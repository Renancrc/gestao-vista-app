"""Worker Celery: roda as tarefas em segundo plano.

Na Fase 2, é aqui que entram as coletas da Graph API (dispositivos, usuários,
grupos e licenças). Por enquanto há só uma tarefa de teste, agendada pelo
"beat" (o relógio do Celery) a cada minuto.
"""

import logging

from celery import Celery

from app.config import get_settings

settings = get_settings()
log = logging.getLogger(__name__)

celery_app = Celery("gestao_vista", broker=settings.redis_url, backend=settings.redis_url)
celery_app.conf.timezone = "America/Sao_Paulo"
celery_app.conf.beat_schedule = {
    "heartbeat-a-cada-minuto": {"task": "app.worker.heartbeat", "schedule": 60.0},
}


@celery_app.task
def heartbeat() -> str:
    """Tarefa de teste: prova que beat -> Redis -> worker está funcionando."""
    log.info("heartbeat: worker vivo")
    return "ok"
