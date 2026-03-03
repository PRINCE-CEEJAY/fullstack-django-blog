from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def add_post(request):
    if request.method == "POST":
        pass
    return render(request, 'posts/add_post.html')

@login_required
def view_posts(request):
    return render(request, 'posts/view_posts.html')