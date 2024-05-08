from .views import Login, signup, profile, songpage, songpage2, songpage3
from django.urls import path
from django.contrib import admin
from django import views
from webpage import views
from . import views
#from website import webpage

urlpatterns = [
   path('', views.home, name = "home"),
   path("Login/", views.Login, name = 'Login'),
   path("signup/", views.signup, name = 'signup'),
   path("profile/", views.profile, name = 'profile'),
   path("songpage/", views.songpage, name = 'songpage'),
   path("songpage2/", views.songpage2, name = 'songpage2'),
   path("songpage3/", views.songpage3, name = 'songpage3'),
]