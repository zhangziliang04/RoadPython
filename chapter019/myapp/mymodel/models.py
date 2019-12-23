from django.db import models

# Create your models here.


# 用户信息类
class UserInfo(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
