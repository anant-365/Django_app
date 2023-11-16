# from django.contrib.sessions.models import Session
# from importlib import import_module
# from django.contrib.auth.middleware import get_user
from django.shortcuts import render, redirect
from js import library as lib
# from django.http import HttpResponse, HttpRequest
# from django.contrib import messages
from .models import Features, UserDetails

# Create your views here.
Login = False
sessionid = str
user = dict
name = str
bio = str
features = Features.objects.all()
username = str


def authenticate(request, session_id):
    if session_id == request.session.session_key:
        return True
    else:
        return False


def login(request):
    global sessionid, Login, user, name, bio, username
    sessionid = str(request.COOKIES['sessionid'])
    if Login and authenticate(request, sessionid):
        return redirect('home')
    if request.method == 'POST':
        e_mail = request.POST['email']
        p_assword = request.POST['password']
        if UserDetails.objects.filter(email=e_mail, password=p_assword).exists():
            user = UserDetails.objects.filter(email=e_mail).values()
            Login = True
            return render(request, '1index.html', {'user': user, 'features': features, 'name': name, 'bio': bio})
        else:
            Login = False
            return redirect('login')
    else:
        return render(request, '42_cloop_login.html')


def home(request):
    if Login is not False:
        global user, name, bio, features
        return render(request, '1index.html', {'features': features, 'user': user})
    else:
        return redirect('login')


def register(request):
    global sessionid, Login, user
    sessionid = str(request.COOKIES['sessionid'])
    if Login and authenticate(request, sessionid):
        return redirect('home')
    if request.method == 'POST':
        try:
            user_name = request.POST['username']
            e_mail = request.POST['email']
            p_assword = request.POST['password']
            b = UserDetails(username=user_name, email=e_mail, password=p_assword)
            b.save()
            Login = True
            return render(request, '1index.html', {'features': features, 'user': user, 'name': name, 'bio': bio})
        except:
            Login = False
            return redirect('register')

    else:
        return render(request, '42.1_cloop_register.html', )


def profileupdate(request):
    global name, bio, username, user
    if request.method == 'POST':
        if Login:
            try:
                for x in user:
                    username = x.get('username')
                name = request.POST['name']
                bio = request.POST['bio']
                UserDetails.objects.filter(username=username).update(name=name, bio=bio)
                user = UserDetails.objects.filter(username=username)
                return render(request,'1index.html',{'user':user})
            except:
                return redirect('profileupdate')
        else:
            return redirect('login')
    else:
        return render(request, 'profile.html')
