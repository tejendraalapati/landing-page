from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login
from .models import contact

# Create your views here.
def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method == 'POST':
        if request.method == 'POST':
            username=request.POST.get('username')
            email=request.POST.get('email')
            pass1=request.POST.get('password1')
            pass2=request.POST.get('password2')

            if pass1!=pass2:
                return HttpResponse("your password and confirm password is not same !!")
            else:
                my_user=User.objects.create_user(username,email,pass1)
                my_user.save()
                return redirect('login')
    return render(request,'signup.html')
    
def login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')

        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            auth_login(request,user)
            return redirect('signup')
        else:
            return HttpResponse("Username and password is incorrect")  
    return render(request,'login.html')

def Contact(request):
    if request.method == 'POST':
        Name=request.POST.get('Name')
        Email=request.POST.get('Email')
        phone_number=request.POST.get('phone')
        Message=request.POST.get('message')
        en=contact(Name=Name,Email=Email,phone_number=phone_number,Message=Message)
        en.save()
        
    return render(request,'contactus.html')