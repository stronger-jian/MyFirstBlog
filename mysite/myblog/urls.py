from django.urls import path

from .import views


app_name = 'myblog'
urlpatterns = [
    path('myblog/', views.index, name='index'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('archives/<int:year>/<int:month>/', views.archives, name='archives'),
    path('category/<int:pk>/', views.category, name='category'),
]