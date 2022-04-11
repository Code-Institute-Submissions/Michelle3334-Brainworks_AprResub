"Blog app views"
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Blog, Comment
from .forms import CommentForm


def all_blogs(request):
    """ A view to return the blog list page"""
    blogs = Blog.objects.all()

    context = {
        'blogs': blogs,
    }

    return render(request, 'blog/blog_post.html', context)


def blog_detail(request, blog_id):
    """ A view to show blog details """

    blog = get_object_or_404(Blog, pk=blog_id)
    comments = blog.comment.order_by('date_created')
    comment = get_object_or_404(Comment)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comment added')
        else:
            messages.error(request, 'Failed to add comment')
 
    context = {
        'blog': blog,
        'comments': comments,
        'comment_form': CommentForm(),
    }

    return render(request, 'blog/blog_detail.html', context)
