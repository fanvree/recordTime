from django.urls import path

# 正在部署的应用的名称
from article import views

app_name = 'article'

urlpatterns = [
    # 目前还没有urls
    path('article-list/', views.article_list, name='article_list'),
    path('article-create/', views.article_create, name='article_create'),
]
