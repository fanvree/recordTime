from django.contrib import admin

# Register your models here.
from django.contrib import admin

# 别忘了导入ArticlerPost
from .models import Article

# 注册ArticlePost到admin中
admin.site.register(Article)
