from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/',views.register,name='register'),
    path('profile/',views.profile,name='profile'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    ##Remove me later
    path('debug/',views.debug,name="debug"),
]