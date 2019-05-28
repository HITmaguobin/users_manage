from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class users_msg(models.Model):
    name=models.CharField(max_length=32)
    password=models.CharField(max_length=32)
    role=models.CharField(max_length=32)
    creator = models.CharField(max_length=32)
    createTime = models.CharField(max_length=32)
    editor = models.CharField(max_length=32)
    editTime=models.CharField(max_length=32)
    isValid=models.CharField(max_length=2)
    def __str__(self):
        return self.name
class url_manage(models.Model):
    url_source=models.CharField(max_length=32)
    link=models.URLField()
    creator = models.CharField(max_length=32)
    createTime = models.CharField(max_length=32)
    timeconfig=models.CharField(max_length=32)
    isValid=models.CharField(max_length=2)