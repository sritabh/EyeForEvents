from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib import messages
from .forms import SignUpForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

#If Not Authenticated show user a path to authenticate i.e. login or register option
#Check whether the user is authenticated if not send user to get authentication
@login_required(login_url='/user/login/')
def home(request):
    return redirect("profile")

#profile page request
@login_required(login_url='/user/login/')
def profile(request):
    return render(request,"user/profile.html")

def login_user(request):
    if request.method == "POST":
        # if someone fills out form , Post it
        username = request.POST["email"]
        password = request.POST["password"]

        #authenticate takes username and password for the cuurent case, checks them against each authentication backend
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # if user exist
            login(request, user)
            messages.success(request, ("You're logged in!!"))
            return redirect("profile")
            # routes to 'profile' on successful login
        else:
            messages.success(request, ("Error logging in!!"))
            return redirect("login")
            # re routes to login page upon unsucessful login
    else:
        return render(request, "user/login.html", {})


def logout_user(request):
    logout(request)
    messages.success(request, ("Youre now logged out"))
    return redirect("home")

#to view register form 
def register(request):
    #request that makes changes in the database - should use POST, in this pass won't come in url
    if request.method == 'POST':
        #creates register form 
        form = SignUpForm(request.POST)
        if form.is_valid():

            #setting email as username
            username = form.cleaned_data['email']
            password = form.cleaned_data['password1']

            #create user , set username & email both as email
            user = User.objects.create_user(username,username,password)

            #store first_name & last_name for profile.html
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']

            #save the user
            user.save()

            #login
            login(request,user)

            #show register msg & redirect to profile
            messages.success(request, ('Youre now registered'))
            return redirect('profile')
    else:
                form = SignUpForm() 
    context = {'form': form}
    return render(request, 'user/register.html', context)


##REMove me later
def debug(request):
    return render(request,'user/debug.html',{'msg':str(request.user)})
