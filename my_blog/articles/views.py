from django.shortcuts import render, HttpResponse
from .models import Article




def articles_list(request):
    articles = Article.objects.all().order_by('date')
    content = {"articles": articles}
    return render(request, 'articles/article_list.html', content)


def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    content = {"article": article}
    return render(request, "articles/article_detail.html", content)
    