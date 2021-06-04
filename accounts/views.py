from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.http import HttpResponse
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']


        if not password == password2:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
        
        if User.objects.filter(username=user_name).exists():
            messages.error(request, 'Username already exists')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return redirect('register')

        user = User.objects.create_user(username=user_name, password=password, email=email, 
                                        first_name=first_name, last_name=last_name)
        #auth.login(request, user)
        #messages.success(request, "Logged in")
        #return redirect('index')

        user.save()
        messages.success(request, 'Registration success')
        return redirect('login')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        return
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

