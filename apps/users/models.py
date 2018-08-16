from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserProfile(AbstractUser):
    name=models.CharField(max_length=32, null=True, blank=True, verbose_name="姓名")
    birthday=models.DateField(null=True, blank=True, verbose_name="出生日期")
    gender=models.CharField(max_length=6, choices=(('male', '男'),('female', '女')), default='male')
    email = models.CharField(max_length=32, null=True, blank=True, verbose_name="邮箱")
    class Meta:
        verbose_name='用户'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name

class VerifyCode(models.Model):
    '''
    短信验证码
    '''
    code=models.CharField(max_length=32, verbose_name='验证码')
    mobile=models.IntegerField(default=0, verbose_name='电话')
    add_time=models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '验证码'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.code