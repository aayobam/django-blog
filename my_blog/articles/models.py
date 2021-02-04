from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User,default=None, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + "..."


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete= models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    comment_text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ('created_on',)


    def __str__(self):
        return "comment by {} on {}".format(self.name, self.created_on)