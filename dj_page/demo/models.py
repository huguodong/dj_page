from __future__ import unicode_literals

from django.db import models

# Create your models here.

# Create your models here.
class user(models.Model):
    UserName = models.CharField(max_length=20)
    UserPwd = models.CharField(max_length=100)
    UserEmail = models.EmailField()
    Phone = models.CharField(max_length=100)
    CreateTime = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)
    is_staff = models.BooleanField(default=1)
