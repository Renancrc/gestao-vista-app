# Gestão à Vista Microsoft

[![CI](https://github.com/Renancrc/gestao-vista-app/actions/workflows/ci.yml/badge.svg)](https://github.com/Renancrc/gestao-vista-app/actions/workflows/ci.yml)

Painel de gestão à vista para ambientes Microsoft: dispositivos do **Intune**, usuários, grupos e licenças do **Entra ID** e indicadores de segurança, num só lugar.

Projeto de portfólio do MBA em Engenharia de Cloud Computing: Python, React, Docker, Kubernetes, Terraform, GitHub Actions e ArgoCD na AWS.

## Arquitetura (local)

| Serviço | Tecnologia | Porta |
|---|---|---|
| frontend | React + Vite + Fluent UI v9, servido pelo nginx | 3000 |
| api | Python 3.12 + FastAPI | 8000 |
| worker / beat | Celery (tarefas em segundo plano e agendamento) | — |
| postgres | PostgreSQL 17 | 5432 |
| redis | Redis 8 (fila do Celery) | — |

## Como rodar

Pré-requisito: Docker. Para desenvolver, abra o repositório no VS Code com **Dev Containers: Reopen in Container**: todas as ferramentas já vêm instaladas.

```bash
cp .env.example .env          # crie o seu .env e troque a senha
docker compose up -d --build  # monta as imagens e sobe tudo
docker compose ps             # todos "running"/"healthy"; migrate "exited (0)"
```

- Painel: http://localhost:3000
- API (documentação interativa): http://localhost:8000/api/docs

Para parar: `docker compose down` (os dados do banco ficam no volume `pgdata`). Para apagar também os dados: `docker compose down -v`.

## Estrutura

```
backend/    API FastAPI, modelos, migrações (Alembic), worker Celery e testes
frontend/   Interface React com Fluent UI (visual do Microsoft 365)
.devcontainer/  Ambiente de desenvolvimento padronizado
docker-compose.yml  Sobe o sistema inteiro localmente
```

## Desenvolvimento

```bash
# Backend
cd backend
uv sync                 # instala as dependências
uv run pytest           # testes
uv run ruff check .     # lint

# Frontend
cd frontend
npm install
npm run dev             # http://localhost:5173 (repassa /api para localhost:8000)
```

## Qualidade

- **pre-commit** (no seu computador, antes de cada commit): espaços e finais de linha, YAML válido, chaves privadas, ruff e gitleaks. Instalado automaticamente no Dev Container; para rodar em tudo: `pre-commit run --all-files`.
- **CI no GitHub Actions** (a cada pull request): lint e testes do backend, lint e build do frontend, busca de segredos no histórico e um teste de integração que sobe o `docker compose` e chama `/api/health`.
