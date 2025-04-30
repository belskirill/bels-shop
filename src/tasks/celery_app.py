from celery import Celery
from src.config import settigns

celery_instance = Celery(
    "tasks",
    broker=settigns.REDIS_URL,
    include=["src.tasks.tasks"],
)


celery_instance.conf.broker_connection_retry_on_startup = True


celery_instance.conf.beat_schedule = {
    "luboe-nazvanie": {
        "task": "chech_not_used_change_password",
        "schedule": 300,
    }
}