from django.contrib import admin


from .models import Article,Category, Tag


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category']

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Tag)
