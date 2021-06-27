from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        psw = request.POST['psw']

        user = auth.authenticate(username=username, password=psw)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You have successfully logged in')
            return redirect('/')
        else:
            messages.info(request, 'Username or Password is incorrect')
            return redirect('login')
    else:
        return render(request, 'login.html')


def reset(request):

    return render(request, 'reset.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        psw1 = request.POST['psw1']
        psw2 = request.POST['psw2']
        email = request.POST['email']
        if psw1 == psw2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=psw1, email=email, first_name=first_name,
                                                last_name=last_name)
                user.save();
                messages.success(request, 'User created successfully')
                return redirect('login')
        else:
            messages.info(request, 'Password not matching')
            return redirect('register')
    return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
