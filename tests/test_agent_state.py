import importlib.util
import io
from pathlib import Path
import tarfile
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('agent_state', Path(__file__).parents[1] / 'ops/agent-state.py')
state = importlib.util.module_from_spec(spec)
spec.loader.exec_module(state)

class AgentStateTests(unittest.TestCase):
    def test_restore_rejects_links_and_traversal(self):
        with tempfile.TemporaryDirectory() as directory:
            base=Path(directory); work=base/'work';work.mkdir(); archive=base/'state.tar.gz'
            with tarfile.open(archive,'w:gz') as tar:
                for name in ['ok.txt','../outside.txt','/absolute.txt']:
                    item=tarfile.TarInfo(name);item.size=4;tar.addfile(item,io.BytesIO(b'test'))
                item=tarfile.TarInfo('link');item.type=tarfile.SYMTYPE;item.linkname='/etc';tar.addfile(item)
                item=tarfile.TarInfo('hard');item.type=tarfile.LNKTYPE;item.linkname='/etc/passwd';tar.addfile(item)
            with patch.object(state,'WORK',work),patch.object(state,'ARCHIVE',archive),patch.object(state.os,'chown'):
                state.restore()
            self.assertEqual([p.name for p in work.iterdir()],['ok.txt'])
            self.assertFalse((base/'outside.txt').exists())

    def test_save_excludes_dependencies_and_symlinks(self):
        with tempfile.TemporaryDirectory() as directory:
            base=Path(directory);work=base/'work';work.mkdir();archive=base/'state.tar.gz'
            (work/'main.py').write_text('print(1)');(work/'node_modules').mkdir()
            (work/'node_modules'/'big').write_text('ignored');(work/'link').symlink_to('/etc/passwd')
            with patch.object(state,'WORK',work),patch.object(state,'ARCHIVE',archive):state.save()
            with tarfile.open(archive) as tar:self.assertEqual(tar.getnames(),['main.py'])

    def test_limit_keeps_previous_snapshot(self):
        with tempfile.TemporaryDirectory() as directory:
            base=Path(directory);work=base/'work';work.mkdir();archive=base/'state.tar.gz';archive.write_bytes(b'previous')
            (work/'large').write_bytes(b'1234')
            with patch.object(state,'WORK',work),patch.object(state,'ARCHIVE',archive),patch.object(state,'MAX_BYTES',3):
                with self.assertRaises(ValueError):state.save()
            self.assertEqual(archive.read_bytes(),b'previous')
