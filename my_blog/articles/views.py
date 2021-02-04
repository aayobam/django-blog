from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Comment
from django.contrib.auth.decorators import login_required
from .forms import CreatArticle, CreateComment



# Articles List.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    content = {"articles": articles}
    return render(request, 'articles/article_list.html', content)


# Each article detail.
@login_required(login_url="/accounts/login")
def article_detail(request, slug):
    template = "articles/article_detail.html"
    articles = get_object_or_404(Article, slug=slug)
    comments = articles.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CreateComment(data=request.POST)
        if comment_form.is_valid():

            # Create a comment object but don't save it
            new_comment = comment_form.save(commit=False)

            # Assign the current post to the comment
            new_comment.article = articles

            # Save the comments to the database
            new_comment.save()
    else:
        comment_form = CreateComment()
    template = "articles/article_detail.html"
    content = {
        "articles": articles,
        "comments": comments,
        "new_comment": new_comment,
        "comment_form": comment_form,
    }
    return render(request, template, content)



# Users articles creating section.
@login_required(login_url="/accounts/login")
def article_create(request):
    if request.method == 'POST':
        form = CreatArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect("articles:list")
    else:
        form = CreatArticle()
    content = {"form": form}
    return render(request, "articles/article_create.html", content)
    