"Blog Admin"
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import BlogPost, Comment


@admin.register(BlogPost)
class BlogPostAdmin(SummernoteModelAdmin):
    "BlogPost admin"
    list_display = (
        'image',
        'title',
        'author',
        'date_authored',
        'text',
        )
    summernote_fields = ('text')


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    "Comment Admin"
    list_display = (
        'blogpost', 
        'author', 
        'text', 
        'date_created',
        )
    summernote_fields = ('text')
