from django import forms
from .models import Article, Comment


# This is an instance of the article creation model class.This returns article creation page to the registered users and authorised users on the blog page .
class CreatArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body', 'slug', 'thumb']
        

# This is an instance of the Comments creation model class. This returns comments form page to the users on the blog page.
class CreateComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'comment_text']
