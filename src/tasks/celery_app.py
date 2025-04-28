from celery import Celery
from src.config import settigns

celery_instance = Celery(
    "tasks",
    broker=settigns.REDIS_URL,
    include=["src.tasks.tasks"],
)


celery_instance.conf.broker_connection_retry_on_startup = True