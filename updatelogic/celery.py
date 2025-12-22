from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'updatelogic.settings')

app = Celery('updatelogic')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'add-dummy-student-every-5-min': {
        'task': 'api.tasks.add_dummy_student',
        'schedule': crontab(minute='*/5'),
    },
}
