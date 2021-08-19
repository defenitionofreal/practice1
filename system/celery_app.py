from __future__ import absolute_import, unicode_literals
import os
from django.conf import settings
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'system.settings.development')

app = Celery('system')

app.conf.enable_utc = False
app.conf.update(timezone='Europe/Moscow')

app.config_from_object('django.conf:settings', namespace='CELERY')

# celery beat
app.conf.beat_schedule = {
    'check-nonce-and-token-every-hour': {
        'task': 'applications.users.tasks.delete_old_nonce_and_token',
        'schedule': crontab(minute=0, hour='*/1')
    }
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
