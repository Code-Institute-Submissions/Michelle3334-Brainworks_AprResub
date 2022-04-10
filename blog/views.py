"Blog app views"
from django.shortcuts import render
from .models import Blog


def all_blogs(request):
    """ A view to return the blog list page"""
    blogs = Blog.objects.all()

    context = {
        'blogs': blogs,
    }

    return render(request, 'blog/blog_post.html', context)
