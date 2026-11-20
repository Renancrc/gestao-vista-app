"""Tabelas do banco. As mudanças viram migrações do Alembic (pasta migrations/)."""

from datetime import datetime

from sqlalchemy import JSON, DateTime, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Tenant(Base):
    """Um tenant Microsoft (Entra ID) monitorado pelo painel."""

    __tablename__ = "tenants"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200))
    # ID do diretório no Entra ID (GUID)
    tenant_id: Mapped[str] = mapped_column(String(36), unique=True)
    # ID do app registration usado para ler a Graph API
    client_id: Mapped[str | None] = mapped_column(String(36))
    is_active: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())


class AuditLog(Base):
    """Registro de cada ação feita por um usuário na plataforma (RF de auditoria)."""

    __tablename__ = "audit_log"

    id: Mapped[int] = mapped_column(primary_key=True)
    tenant_id: Mapped[int | None] = mapped_column(ForeignKey("tenants.id"))
    actor: Mapped[str] = mapped_column(String(320))  # e-mail/UPN de quem fez
    action: Mapped[str] = mapped_column(String(100))  # ex.: login, export, config.update
    target: Mapped[str | None] = mapped_column(String(200))
    details: Mapped[dict | None] = mapped_column(JSON)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), index=True
    )
