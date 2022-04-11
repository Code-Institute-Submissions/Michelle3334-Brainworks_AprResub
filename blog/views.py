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
    comments = blog.comment.order_by('-date_created')
    new_comment = None
    

    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.blog = blog
            new_comment.author = request.user.userprofile
            new_comment.save()
            messages.success(request, 'Comment added')
        else:
            form = CommentForm()
            messages.error(request, 'Failed to add comment')
 
    context = {
        'blog': blog,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': CommentForm(),
    }

    return render(request, 'blog/blog_detail.html', context)
