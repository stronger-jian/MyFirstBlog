from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    """ 分类 """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    """ 标签 """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    """ 文章 """
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True, null=True) # 文章摘要
    category = models.ForeignKey(Category, on_delete=True)
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    views = models.PositiveIntegerField(default=0) # 文章的阅读量

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('myblog:detail', kwargs={
            'pk': self.pk,
        })

    class Meta:
        ordering = ['-created_time']