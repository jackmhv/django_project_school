from hashlib import new
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Examscore
from django.contrib.auth.models import User
# Create your views here.
def HomePage(request):
    #return HttpResponse('<h1>Hello jackmhv</h1>')
    return render (request,'school/home.html')
def AboutPage(request):
    return render(request,'school/about.html')
def ContactUs(request):
    return render(request, 'school/contactus.html')
def ShowScore(request):
    score = Examscore.objects.all() #being from by Database
    context = {'score':score}
    return render (request, 'school/showscore.html', context)
def Register(request):
    if request.method == 'POST':
        data = request.POST.copy()
        name = data.get('name')
        lastname = data.get('lastname')
        email = data.get('email')
        password = data.get('password')
        
        newuser = User()
        newuser.username = email
        newuser.first_name = name
        newuser.last_name = lastname
        newuser.email = email
        newuser.set_password(password)
        newuser.save()
        return redirect('home-page')
    return render (request, 'school/register.html')
def Login (request):
    return render (request, 'school/login.html')
