"""second_case URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='post_list_url'),
    path('post/create/', views.PostCreate.as_view(), name='post_create_url'),
    path('post/<str:slug>/', views.PostDetail.as_view(), name='post_detail_url'),
    path('post/<str:slug>/update/', views.PostUpdate.as_view(), name='post_update_url'),
    path('tags/', views.tags_list, name='tags_list_url'),
    path('tag/create/', views.TagCreate.as_view(), name='tag_create_url'),
    path('tag/<str:slug>/', views.TagDetail.as_view(), name='tag_detail_url'),
    path('tag/<str:slug>/update/', views.TagUpdate.as_view(), name='tag_update_url'),


]

