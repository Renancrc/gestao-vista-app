"""Ponto de entrada da API (FastAPI)."""

from typing import Annotated, Literal

from fastapi import APIRouter, Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.config import get_settings
from app.db import get_session

settings = get_settings()

# Sessão do banco injetada pelo FastAPI em cada requisição
SessionDep = Annotated[Session, Depends(get_session)]

# Todas as rotas ficam em /api: assim a API funciona igual acessada direto
# (porta 8000) ou pelo nginx do frontend (porta 3000)
app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    docs_url="/api/docs",
    redoc_url=None,
    openapi_url="/api/openapi.json",
)
router = APIRouter(prefix="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_methods=["*"],
    allow_headers=["*"],
)


class HealthResponse(BaseModel):
    """Formato da resposta do /api/health (aparece na documentação em /api/docs)."""

    status: Literal["ok", "degraded"]
    version: str
    environment: str
    database: Literal["ok", "error"]


@router.get("/health", tags=["infra"])
def health(session: SessionDep) -> HealthResponse:
    """Mostra se a API está no ar e se consegue falar com o banco.

    Usado pelo frontend, pelo docker compose e, na Fase 3, pelo Kubernetes.
    """
    try:
        session.execute(text("SELECT 1"))
        database = "ok"
    except Exception:  # noqa: BLE001 - qualquer falha de banco vira "error"
        database = "error"

    return HealthResponse(
        status="ok" if database == "ok" else "degraded",
        version=app.version,
        environment=settings.environment,
        database=database,
    )


app.include_router(router)
