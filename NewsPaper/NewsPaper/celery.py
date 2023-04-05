import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPaper.settings')

app = Celery('NewsPaper')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'action_every_monday_8am': {
        'task': 'action',
        'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
        'args': (),
    },
}





# import redis
#
# red = redis.Redis(
#     host='redis-19444.c61.us-east-1-3.ec2.cloud.redislabs.com',
#     port=19444,
#     password='YYFb7a36cMjB47c4rlLrDeigIynn39Qh'
# )