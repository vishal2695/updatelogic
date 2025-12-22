from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'updatelogic.settings')

app = Celery('updatelogic')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()



from celery.schedules import crontab

app.conf.beat_schedule = {
    'add-dummy-every-2-min': {
        'task': 'api.tasks.add_dummy_student',
        'schedule': crontab(minute='*/2'),
    },
}

