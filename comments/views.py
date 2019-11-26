from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post
from django.views.decorators.http import require_POST
from django.contrib import messages

from .forms import CommentForm



@require_POST
def comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    form = CommentForm(request.POST)

    if form.is_valid():
        c = form.save(commit=False)
        c.post = post
        c.save()
        messages.add_message(request, messages.SUCCESS, '评论发布成功！', extra_tags='success')
        return redirect(post)

    context = {
        'post': post,
        'form': form,
    }
    messages.add_message(request, messages.ERROR, '评论发表失败！请修改表单中的错误后重新提交。', extra_tags='danger')
    return render(request, 'comments/preview.html', context=context)


