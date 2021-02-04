from django import forms
from .models import Article, Comment


class CreatArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body', 'slug', 'thumb']


class CreateComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'comment_text']