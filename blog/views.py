"Blog app views"
from django.shortcuts import render


def bloglist(request):
    """ A view to return the blog list page"""
    return render(request, 'blog/blog_post.html')
