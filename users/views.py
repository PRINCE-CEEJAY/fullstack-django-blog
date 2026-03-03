from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('homepage')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.username == 'admin':
                return redirect('admin:index')
            login(request, user)
            return redirect('homepage')
    else:
        form = AuthenticationForm()
        return render(request, 'users/login.html', {'form': form})

def logout(request):
    logout(request)
    return redirect('login')
