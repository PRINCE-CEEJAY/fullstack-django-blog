from django.urls import path
from . import views

urlpatterns = [
    path('add_post/', views.add_post, name='add_post'),
    path('view_posts/', views.view_posts, name='view_posts'),
]