
from celery_task.main import celery_app

@celery_app.task(name="add_together")
def add_together(a,b):
    return a+b
