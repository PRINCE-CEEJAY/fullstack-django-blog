from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import POST
# Create your views here.

@login_required
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

@login_required
def view_posts(request):
    posts = POST.objects.all().order_by('-createdAt') # sort in descending date order
    return render(request, 'posts/view_posts.html', {'posts': posts})