from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='news-home'),
    path('news/', views.news, name='search-news'),
    path('history/', views.history, name='search-history'),
    path('trends/', views.trends, name='trends'),
]