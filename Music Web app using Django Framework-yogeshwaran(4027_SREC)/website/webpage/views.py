from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
# Create your views here.

#def display(request):
 #  return HttpResponse("welcome all")

def Login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to homepage after login
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

   #return HttpResponse()


def signup(request):
   if request.method == 'POST':
      form = SignUpForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('home')
   
   else:
      form = SignUpForm()
   return render(request, 'signup.html', {'form':form})

def home(request):
   return render(request, 'home.html')

def profile(request):
   return render(request, 'profile.html')

def songpage(request):
   return render(request, 'songpage.html')

def songpage2(request):
   return render(request, 'songpage2.html')

def songpage3(request):
   return render(request, 'songpage3.html')