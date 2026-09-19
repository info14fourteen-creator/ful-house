"""Restore Fullhouse model and tool configuration on every web start."""
from pathlib import Path
import logging
import os

MODEL_ID = 'huihui_ai/qwen3-coder-abliterated:30b'
OPENAI_MODEL_ID = 'fullhouse-codex-api'
TOOL_ID = 'fulhouse_engineer'

log = logging.getLogger(__name__)


class _Request:
    def __init__(self, app):
        self.app = app


async def configure_engineer(upstream):
    """Upsert the coding tool and model wrapper using Open WebUI's own stores."""
    try:
        from open_webui.models.models import ModelForm, Models
        from open_webui.models.tools import ToolForm, ToolMeta, Tools
        from open_webui.models.users import Users
        from open_webui.utils.plugin import get_tools_cache, load_tool_module_by_id, replace_imports
        from open_webui.utils.tools import get_tool_specs
    except Exception:
        log.exception('Fullhouse bootstrap imports failed')
        return

    user = await Users.get_user_by_email('steelstan@ful.house')
    if not user:
        log.warning('Fullhouse bootstrap skipped: admin user is not ready')
        return

    root = Path(__file__).resolve().parent.parent
    tool_content = replace_imports((root / 'ops' / 'engineer-tool.py').read_text())
    rules = (root / 'app' / 'engineer-rules.md').read_text()

    tool_module, frontmatter = await load_tool_module_by_id(TOOL_ID, content=tool_content)
    tools_cache = get_tools_cache(_Request(upstream))
    tools_cache[TOOL_ID] = tool_module
    specs = get_tool_specs(tool_module)

    tool_form = ToolForm(
        id=TOOL_ID,
        name='Fullhouse engineering',
        content=tool_content,
        meta=ToolMeta(
            description='Scoped repository, deployment and isolated coding workspace tools',
            manifest=frontmatter,
            has_user_valves=hasattr(tool_module, 'UserValves'),
        ),
        access_grants=[],
    )
    existing_tool = await Tools.get_tool_by_id(TOOL_ID)
    if existing_tool:
        await Tools.update_tool_by_id(
            TOOL_ID,
            {
                **tool_form.model_dump(exclude={'id'}),
                'specs': specs,
            },
        )
    else:
        await Tools.insert_new_tool(user.id, tool_form, specs)

    async def upsert_model(model_id, name, base_model_id, openai_chat=False):
        existing_model = await Models.get_model_by_id(model_id)
        params = dict(existing_model.params.model_dump() if existing_model else {})
        params.update({'system': rules, 'function_calling': 'native'})
        if openai_chat:
            # OpenAI chat/completions rejects function tools when reasoning_effort is set.
            # Keep reasoning disabled for this wrapper; true Codex reasoning uses openai_codex.
            params['reasoning_effort'] = 'none'
            params.pop('reasoning', None)
        meta = dict(existing_model.meta.model_dump() if existing_model else {})
        meta['knowledge'] = None
        meta['toolIds'] = [TOOL_ID]
        form = ModelForm(
            id=model_id,
            base_model_id=base_model_id,
            name=name,
            params=params,
            meta=meta,
            access_grants=[],
            is_active=True,
        )
        if existing_model:
            await Models.update_model_by_id(model_id, form)
        else:
            await Models.insert_new_model(form, user.id)

    await upsert_model(MODEL_ID, 'Fullhouse Local', None)
    await upsert_model(
        OPENAI_MODEL_ID,
        'Fullhouse OpenAI API',
        os.getenv('FULHOUSE_OPENAI_CHAT_MODEL', 'gpt-5.6-sol'),
        openai_chat=True,
    )
    log.warning('Fullhouse bootstrap configured models=%s,%s tool=%s', MODEL_ID, OPENAI_MODEL_ID, TOOL_ID)
