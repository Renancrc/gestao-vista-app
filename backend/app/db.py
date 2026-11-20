"""Conexão com o banco de dados (SQLAlchemy 2)."""

from collections.abc import Iterator

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from app.config import get_settings

# pool_pre_ping: testa a conexão antes de usar, evitando erro depois que o banco reinicia
engine = create_engine(get_settings().database_url, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


class Base(DeclarativeBase):
    """Classe base de todas as tabelas (modelos)."""


def get_session() -> Iterator[Session]:
    """Abre uma sessão por requisição e fecha no final (dependência do FastAPI)."""
    with SessionLocal() as session:
        yield session
