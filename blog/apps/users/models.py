from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):

    """
       blank 默认是flase 如果为true 字段允许为空
       null          如果True，Django将NULL在数据库中存储空值。默认是False
    """
    GENDER_CHOICES = (
        ('male',"男"),
        ("female","女")
    )
    gender = models.CharField(max_length=16,choices=GENDER_CHOICES,default="female",verbose_name="性别")
    mobile = models.CharField(max_length=11,blank=True,null=True,verbose_name="电话",unique=True)
    top_img = models.ImageField(max_length=200,null=True,upload_to='user/')
    create_time = models.DateTimeField(default=datetime.now,verbose_name="创建时间")
    email_active = models.BooleanField(default=False, verbose_name='邮箱验证状态')

    class Meta:
        db_table="users"
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
