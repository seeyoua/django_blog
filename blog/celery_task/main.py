import os
from celery import Celery
from celery_task import config

#为celery使用django配置文件进行设置
if not os.getenv("DJANGO_SETTINGS_MODULE"):
    os.environ["DJANGO_SETTINGS_MODULE"] = "blog.settings"

celery_app = Celery("blog")

#导入celery配置
celery_app.config_from_object("celery_task.config")
#注册celery任务
celery_app.autodiscover_tasks(["celery_task.count"])
