from django.conf.urls import url
from django.urls import path
from articles.views import(
    article_list, 
    article_detail, 
    article_create
)

app_name = 'articles'


urlpatterns = [
    path('create/', article_create, name="create"),
    path('list', article_list, name="list"),
    path('<str:slug>/detail', article_detail, name="detail"),
]
