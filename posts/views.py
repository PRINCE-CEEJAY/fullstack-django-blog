from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post

# Create your views here.
def add_post(request):
    if request.method == 'POST':
        data = request.POST

        title = data.get('title')
        body = data.get('body')

        if not title or not body:
            return HttpResponse('<h1> All fields are required </h1>')
        
        new_post = Post(title=title, body=body)
        new_post.save()
        return redirect('show_posts')
        


    return render(request, 'posts/add_post.html')

def show_posts(request): 
    posts = Post.objects.all()
    return render(request, 'posts/show_posts.html', {'posts': posts})