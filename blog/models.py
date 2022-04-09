"""Blog Post models"""
from django.db import models
from profiles.models import UserProfile


class BlogPost(models.Model):
    "Blog post model"
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(
        UserProfile, on_delete=models.DO_NOTHING, related_name='blog')
    date_authored = models.DateTimeField(auto_now=True)
    text = models.TextField()

    class Meta:
        ordering = ['-date_authored']

    def __str__(self):
        return self.title


class Comment(models.Model):
    "Blog comment model"
    blogpost = models.ForeignKey(
        BlogPost, on_delete=models.CASCADE, related_name='comment')
    author = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return f'Comment {self.text} by {self.author}'
