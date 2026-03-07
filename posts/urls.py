from django.urls import path
from posts import views

app_name = 'posts'
urlpatterns = [
    path('add_post/', views.add_post, name='add_post'),
    path('view_posts/', views.view_posts, name='view_posts'),
    path('delete_post/<int:id>', views.delete_post, name='delete_post'),
    path('update_post/<int:id>', views.update_post, name='update_post'),
]