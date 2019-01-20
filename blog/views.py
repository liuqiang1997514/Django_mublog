from django.shortcuts import render
from . import models
import datetime
from django.http import HttpResponse


# Create your views here.
# 逻辑处理

def home(request):
    articles = models.Article.objects.all()
    return render(request, 'blog/home.html', {'articles': articles})


def article_show(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_show.html', {'article': article})


def article_edit(request, article_id):
    if str(article_id) == '0':
        return render(request, 'blog/article_edit.html')
    else:
        article = models.Article.objects.get(pk=article_id)
        return render(request, 'blog/article_edit.html', {'article': article})


def edit_action(request):
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    article_id = request.POST.get('id', '0')
    if str(article_id) == '0':
        models.Article.objects.create(title=title, content=content, pub_time=datetime.datetime.now())
    else:
        article = models.Article.objects.get(pk=article_id)
        article.title = title
        article.content = content
        article.save()

    articles = models.Article.objects.all()
    return render(request, 'blog/home.html', {'articles': articles})