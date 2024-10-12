from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('all-posts/', views.all_posts, name='all_posts_page'),
  path('posts/<slug:slug>/', views.post_detail, name='post_detail_page'),
]