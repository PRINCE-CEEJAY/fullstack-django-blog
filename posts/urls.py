from django.urls import path
from . import views

urlpatterns = [
    path('add_post/', views.add_post, name='add_post'),
    path('show_posts/', views.show_posts, name='show_posts'),
    path('delete_post/<int:id>', views.delete_post, name='delete_post'),
    path('update_post/<int:id>', views.update_post, name='update_post'),
]