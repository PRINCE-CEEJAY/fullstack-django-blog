from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
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

@login_required(login_url='login')
def show_posts(request): 
    posts = Post.objects.all()
    return render(request, 'posts/show_posts.html', {'posts': posts})

@login_required(login_url='login')
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    if post:
        post.delete()
        return redirect('show_posts')
    return HttpResponse(f"Post with the ID {id} does not exist")


@login_required(login_url='login')
def update_post(request, id):
    if request.method == "POST":
        post = get_object_or_404(Post, id=id)
        title = request.POST.get('title')
        body = request.POST.get('body')

        if post:
            if title:
                post.title = title
            if body:
                post.body = body
            post.save()
            return redirect('show_posts')
        return HttpResponse(f"Post with the ID {id} does not exist")
    return HttpResponse(f"METHOD NOT ALLOWED")
    

