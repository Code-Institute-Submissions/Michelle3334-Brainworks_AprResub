"Blog app views"
from django.shortcuts import render
from .models import BlogPost


def all_blogs(request):
    """ A view to return the blog list page"""
    blogposts = BlogPost.objects.all()

    return render(request, 'blog/blog_post.html')
