from celery import Celery
from celery.schedules import crontab

celery = Celery(__name__, broker='redis://localhost:6379/0')

celery.conf.beat_schedule = {
    'midnight-task': {
        'task': 'app.tasks.midnight_task',
        'schedule': crontab(minute=0, hour=0),
    }
}
