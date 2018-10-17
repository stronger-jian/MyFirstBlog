from django.urls import path
from . import views


app_name = 'comment'

urlpatterns = [
    path('comment/article/<int:pk>/', views.sub_comment, name='aritcle_comment')
]