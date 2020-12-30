from django.conf.urls import url
from django.urls import path
from articles.views import(articles_list, article_detail)

app_name = 'articles'


urlpatterns = [
    path('', articles_list, name="list"),
    path('<str:slug>/detail', article_detail, name="detail")
]
