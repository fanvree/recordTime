from django.db import models
from django.utils import timezone


class Article(models.Model):
    createdTime = models.FloatField(default=0)
    visualTime = models.DateTimeField(default=timezone.now)
    owner = models.CharField(max_length=200, default='test')
    keyword = models.CharField(max_length=1000, default='')
    content = models.CharField(max_length=10000)


class Meta:
    db_table = 'Article'
