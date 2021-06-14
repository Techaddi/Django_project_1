from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

def signup(request):
    if request.method =='POST':
        first_name =request.POST['first_name']
        last_name =request.POST['last_name']
        username =request.POST['username']
        password1 = request.POST['password1']
        password2 =request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'User name already exists')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,email=email,password=password1,first_name=first_name,last_name=last_name)
                user.save()
                messages.info(request,'Registration Successfully')
                return redirect('login')
        else:
            messages.info(request,'Incorrect confirm password')
            return redirect('signup')
            
    else:
         return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username =request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

# Create your views here.
