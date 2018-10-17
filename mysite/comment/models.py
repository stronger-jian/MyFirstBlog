from django.db import models

from myblog.models import Article


class Comment(models.Model):
    """ 评论 """
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    website = models.URLField(blank=True, null=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    article = models.ForeignKey(Article, on_delete=True)
