from django.urls import path
from .import views
from .views import PostDeleteView
from .views import PostEditView
from .views import PostCreateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import views as auth_views 

urlpatterns = [
    #path ('', views.post_list, name='post_list'),
    path('', views.PostListView.as_view(), name='post_list'),
    #path('<int:pk>', views.post_detail, name='post_detail'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    #path('post/new/', views.post_new, name='post_new'),
    #path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/edit/', PostEditView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

