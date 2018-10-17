from django import template
from ..models import Article, Category


register = template.Library() # 注册tags


@register.simple_tag
def get_recent_articles(num=5):
    """ 最新文章模板标签 """
    return Article.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def archives():
    """ 归档模板标签 """
    return Article.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    """ 分类模板标签 """
    return Category.objects.all()


