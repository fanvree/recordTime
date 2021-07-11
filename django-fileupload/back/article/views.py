import json

from django.core import serializers
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# 视图函数
from django.utils import timezone

from article.models import Article


def article_list(request):
    if request.method == 'GET':
        if request.GET.get("secret_key") != 'record':
            return HttpResponse(status=404)
        if request.GET.get("owner") is not None:
            articles = Article.objects.filter(owner=request.GET.get("owner")).all()
        else:
            articles = Article.objects.all()
        resp = serializers.serialize("json", articles)
        return HttpResponse(resp, content_type="application/json")
    return HttpResponse(status=404)


def article_create(request):
    if request.method == 'GET':
        if request.GET.get("secret_key") != 'record':
            return HttpResponse(status=404)
        if request.GET.get("content") is not None:
            owner = 'test'
            keyword = ''
            if request.GET.get("owner") is not None:
                owner = request.GET.get("owner")
            if request.GET.get("keyword") is not None:
                keyword = request.GET.get("keyword")
            Article.objects.create(content=request.GET.get("content"), owner=owner,
                                   keyword=keyword, createdTime=timezone.now().timestamp())
            return HttpResponse("ok", content_type='text/plain')
        return HttpResponse("require key CONTENT", content_type='text/plain', status=400)
    return HttpResponse(status=404)
