from django.shortcuts import render, get_object_or_404,redirect
from myblog.models import Article
from django.urls import reverse


from .models import Comment
from .forms import CommentForm


def sub_comment(request, pk):
    """ 评论 """
    # 获取被评论的 文章
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect(article)
        else:
            comment_list = article.comment_set.all()
            context = {
                'article': article,
                'form': form,
                'comment_list': comment_list,
            }
        return render(request, 'myblog/detail.html', context)
    return redirect(article)



