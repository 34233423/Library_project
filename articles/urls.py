# articles/urls.py

from django.urls import path
from .views import search, home, article_detail

urlpatterns = [
    path('search/', search, name='search'),
    path('article/<int:article_id>/', article_detail, name='article_detail'),
    path('', home, name='home'),
]
