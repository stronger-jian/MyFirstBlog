import markdown
from django.shortcuts import render, get_object_or_404
from comment.forms import CommentForm


from .models import Article, Category
from comment.forms import CommentForm

# Create your views here.


# def index(request):
#     """ 主页 """
#     article_list = Article.objects.all()
#     limit = 5
#     paginator = Paginator(article_list, limit)
#     page = request.GET.get('page', 1)
#     try:
#         articles = paginator.page(page)
#     except PageNotAnInteger:
#         articles = paginator.page(1)
#     except EmptyPage:
#         articles = paginator.page(paginator.num_pages)
#
#     return render(request, 'myblog/index.html', {'articles': articles})
def index(request):
    article_list = Article.objects.all()
    return render(request, 'myblog/index.html', context={
        'article_list': article_list,
    })


# def detail(request, pk):
#     article = get_object_or_404(Article,pk=pk)
#     form = CommentForm()
#     comment_list = article.comment_set.all()
#     context = {
#         'article': article,
#         'form': form,
#         'comment_list': comment_list,
#     }
#     return render(request, 'myblog/article.html', context)
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.body = markdown.markdown(article.body,
                                    extensions=[
                                        'markdown.extensions.extra',
                                        'markdown.extensions.codehilite',
                                        'markdown.extensions.toc',
                                    ]
    )
    form = CommentForm()
    comment_list = article.comment_set.all()
    return render(request, 'myblog/detail.html', context={
        'article': article,
        'form': form,
        'comment_list': comment_list,
    })


def archives(request, year, month):
    article_list = Article.objects.filter(
                                        created_time__year=year,
                                        created_time__month=month
    )
    return render(request, 'myblog/index.html', context={'article_list': article_list})


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    article_list = Article.objects.filter(category=cate)
    return render(request, 'myblog/index.html', context={'article_list': article_list})