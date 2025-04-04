from django.contrib import admin
from django.urls import path

from django.conf import settings # import settings.py
from django.conf.urls.static import static # for static
from . import views

urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),
    path('create/', views.tweet_create, name='tweet_create'),
    path('<int:Twitter_id>/update/', views.tweet_update, name = 'tweet_update'),
    path('<int:Twitter_id>/delete/', views.tweet_delete, name = 'tweet_delete'),
    path('register/', views.register, name = 'register'),
    path('search/', views.search, name='search'),

]