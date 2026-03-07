from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('users:dashboard')    
        return render(request, 'users/register.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'users/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            member = form.get_user()

            login(request, member)
            # redirect admin to admin panel and any other user to dashboard
            if member.is_staff:
                return redirect('admin:index')
            return redirect('users:dashboard')
        # if user details is invalid, send back to login page
        return render(request, 'users/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'users/login.html', {'form': form})
    
def logout_view(request):
    logout(request)
    return redirect('users:login')


@login_required(login_url='users:login')
def dashboard(request):
    return render(request, 'users/dashboard.html')


