from django.urls import path
from . import views

urlpatterns = [
    path('add_post/', views.add_post, name='add_post'),
    path('show_posts/', views.show_posts, name='show_posts'),
]