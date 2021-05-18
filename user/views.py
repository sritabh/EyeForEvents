from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib import messages
from.forms import SignUpForm
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("User app contains anything related to user signup,login etc")

#profile page request
def profile(request):
    return render(request,"user/profile.html")

def login_user(request):
    if request.method == "POST":
        # if someone fills out form , Post it
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # if user exist
            login(request, user)
            messages.success(request, ("Youre logged in"))
            return redirect("home")
            # routes to 'home' on successful login
        else:
            messages.success(request, ("Error logging in"))
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
            form.save()
            username = form.cleaned_data['email']
            #email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, ('Youre now registered'))
            return redirect('profile')
    else:
                form = SignUpForm() 
    context = {'form': form}
    return render(request, 'user/register.html', context)
