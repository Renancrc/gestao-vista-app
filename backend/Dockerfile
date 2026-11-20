# syntax=docker/dockerfile:1
# Imagem do backend. A mesma imagem roda a API, o worker e o beat;
# o que muda é o comando (ver docker-compose.yml).

# ---------- Estágio 1: instala as dependências ----------
FROM python:3.12-slim AS builder

# uv: gerenciador de pacotes Python (copiado da imagem oficial)
COPY --from=ghcr.io/astral-sh/uv:0.13 /uv /usr/local/bin/uv

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

WORKDIR /app

# Copia só os arquivos de dependência primeiro: se o código mudar e as
# dependências não, o Docker reaproveita esta camada (build mais rápido)
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

# ---------- Estágio 2: imagem final, só com o necessário ----------
FROM python:3.12-slim AS runtime

# Usuário sem privilégio de root (boa prática de segurança)
RUN useradd --create-home --uid 1000 app

WORKDIR /app
COPY --from=builder /app/.venv /app/.venv
COPY alembic.ini ./
COPY migrations ./migrations
COPY app ./app

ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1

USER app
EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
