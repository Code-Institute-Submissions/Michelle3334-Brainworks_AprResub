"Blog Admin"
from django.contrib import admin
from .models import Blog, Comment


class BlogAdmin(admin.ModelAdmin):
    "Blog admin"
    list_display = (
        'title',
        'author',
        'date_authored',
        'text',
        'image',
        )

    ordering = ('title',)


class CommentAdmin(admin.ModelAdmin):
    "Comment Admin"
    list_display = (
        'blog', 
        'author', 
        'text', 
        'date_created',
        )

admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
