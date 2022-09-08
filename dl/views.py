from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth import get_user_model

from Home.views import Home
User = get_user_model()
# Create your views here.


def handlesignup(request):
    global signup_status
    signup_status=""
    if request.method == 'POST':
        email=request.POST['email']
        Password=request.POST['Password']
        users = User.objects.create_user(email,Password)
        signup_status="Success"
        

def signup_page(request):
    handlesignup(request)
    return render(request,'signup.html', {'signup_status':signup_status} )


def handlelogin(request):
    if request.method == 'POST':
        lemail=request.POST['lemail']
        lPassword=request.POST['lPassword']
        User = authenticate(email=lemail,password=lPassword)
        if User is not None:
            login(request,User)
            print("success login")
            return redirect(Home)
        else:
            print("invalid")
    return render(request,'login.html')

def handlelogout(request):
    logout(request)
    print("succes logout")
    return redirect(Home)
