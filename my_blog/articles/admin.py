from django.contrib import admin
from .models import Article, Comment


# This registers the Article table at the Admin area
@admin.register(Article)
class AdminArticle(admin.ModelAdmin):
    list_display = ("title", "body", "thumb", "author", "date")
    search_fields = ("title", "date", "body")
    list_filter = ("author", "date")
    

# This registers the Comment Table at the Admin area
@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    list_display = ('name', 'email', 'article','comment_text', 'created_on', 'active')
    list_filter = ('created_on', 'active')
    search_fields = ('name', 'email', 'comment_text')
    actions = ["approve_comments"]

    # This function display active comments on a article by users which has been approved as active by the Administrator.
    def approve_comments(self, request, queryset):
        return queryset.update(active=True)
