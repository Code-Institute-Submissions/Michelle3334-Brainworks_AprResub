"Blog app views"
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import BlogPost


def BlogPostList(request):
    model = BlogPost
    queryset = BlogPost.objects.order_by("-date_authored")
    template_name = "blog_post.html"
    paginate_by = 6

    return render(request, 'blog/blog_post.html')
