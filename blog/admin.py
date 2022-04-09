"Blog Admin"
from django.contrib import admin
from .models import BlogPost, Comment


class BlogPostAdmin(admin.ModelAdmin):
    "BlogPost admin"
    list_display = (
        'title',
        'author',
        'date_authored',
        'text',
        )


class CommentAdmin(admin.ModelAdmin):
    "Comment Admin"
    list_display = (
        'blogpost', 
        'author', 
        'text', 
        'date_created',
        )


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment, CommentAdmin)
