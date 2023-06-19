from django.shortcuts import render, redirect
from apps.todo.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            if password == confirm_password:
                user = User.objects.create(username = username, email = email)
                user.set_password(password)
                user.save()
                user = authenticate(username = username, password = password)
                login(request, user)
                return redirect('index')
            else:
                return redirect('index')
    return render(request, 'register.html')
    
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            try:
                user = User.objects.get(username = username)
                user = authenticate(username = username, password = password)
                login(request, user)
                return redirect('index')
            except:
                return redirect('login')
        else:
            return redirect('login')
    return render(request, 'login.html')


    