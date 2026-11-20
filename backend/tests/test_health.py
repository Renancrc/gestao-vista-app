"""Testes da rota /api/health.

Os testes não dependem de PostgreSQL: trocamos a sessão do banco por uma
de SQLite em memória (override de dependência do FastAPI).
"""

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.db import get_session
from app.main import app


def _sqlite_session():
    engine = create_engine("sqlite://")
    with Session(engine) as session:
        yield session


class _BrokenSession:
    def execute(self, *_args, **_kwargs):
        raise RuntimeError("banco fora do ar")


def test_health_ok():
    app.dependency_overrides[get_session] = _sqlite_session
    try:
        response = TestClient(app).get("/api/health")
    finally:
        app.dependency_overrides.clear()

    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"
    assert body["database"] == "ok"


def test_health_banco_fora_do_ar():
    app.dependency_overrides[get_session] = lambda: _BrokenSession()
    try:
        response = TestClient(app).get("/api/health")
    finally:
        app.dependency_overrides.clear()

    assert response.status_code == 200
    assert response.json() == {
        "status": "degraded",
        "version": "0.1.0",
        "environment": "local",
        "database": "error",
    }
