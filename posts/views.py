from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from posts.models import POST


@login_required(login_url='users:login')
def add_post(request):
    if request.method == "POST":
        data = request.POST
        title = data.get('title')
        text = data.get('text')

        if not title or not text:
            return render(request, 'posts/add_post.html')
        
        new_post = POST(title=title.upper(), text=text)
        new_post.save()
        return redirect('view_posts')
    else:            
        return render(request, 'posts/add_post.html')

@login_required(login_url='users:login')
def view_posts(request):
    posts = POST.objects.all().order_by('-createdAt') # sort in descending date order
    return render(request, 'posts/view_posts.html', {'posts': posts})

from django.shortcuts import get_object_or_404

@login_required(login_url='users:login')
def delete_post(request, id):
    if request.method == "POST":
        post = get_object_or_404(POST, id=id)
        post.delete()
        return redirect('view_posts')
    return HttpResponse("METHOD NOT ALLOWED!")


@login_required(login_url='users:login')
def update_post(request, id):
    post = get_object_or_404(POST, id=id)

    if request.method == "POST":
        title = request.POST.get('title')
        text = request.POST.get('text')

        if title:
            post.title = title.upper()
        if text:
            post.text = text

        post.save()
        return redirect('view_posts')

    return render(request, 'posts/update_post.html', {'post': post})

      
