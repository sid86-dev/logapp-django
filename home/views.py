from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm
from .models import CreateUserForm
from django.contrib.auth.models import User
# from pprint import pprint # new
# user=User.objects.get(id=2)
# pprint(user.__dict__)
# Create your views here.
def home(request):
    details = User.objects.all()
    context = {
        'users': details
        }
    
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html', context)

def signupuser(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    context = {'form':form}
    return render(request, 'signup.html', context)    
def loginuser(request):
    if request.method == "POST":
        # check user's credentials
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
    # A backend authenticated the credentials   
        else:
            return render(request, 'login.html')
    # No backend authenticated the credentials
    return render(request, 'login.html')
def logoutuser(request):
    logout(request)
    return redirect("/login")
