FROM ghcr.io/open-webui/open-webui:v0.11.3-slim
USER root
RUN apt-get update && apt-get install -y --no-install-recommends openssh-client && rm -rf /var/lib/apt/lists/*
COPY app /app/backend/app
COPY app/static/homebrew.css /app/backend/open_webui/static/homebrew.css
COPY app/static/matrix.js /app/backend/open_webui/static/matrix.js
RUN python -c "from pathlib import Path;p=Path('/app/build/index.html');s=p.read_text();p.write_text(s.replace('</head>','<link rel=\"stylesheet\" href=\"/static/homebrew.css\"><script defer src=\"/static/matrix.js\"></script></head>'))"
ENV ENABLE_SIGNUP=false ENABLE_PERSISTENT_CONFIG=false ENABLE_OPENAI_API=false ENABLE_OLLAMA_API=true OLLAMA_BASE_URL=http://127.0.0.1:11434 ENABLE_VERSION_UPDATE_CHECK=false ENABLE_COMMUNITY_SHARING=false ENABLE_EVALUATION_ARENA_MODELS=false WEBUI_URL=https://ful.house WEBUI_NAME=Fullhouse DEFAULT_MODELS=huihui_ai/qwen3-coder-abliterated:30b RAG_EMBEDDING_ENGINE=ollama ENABLE_RAG_WEB_SEARCH=false ENABLE_CODE_EXECUTION=false ENABLE_CODE_INTERPRETER=false DATA_DIR=/tmp/openwebui
WORKDIR /app/backend
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8080} --proxy-headers --forwarded-allow-ips='*'"]
