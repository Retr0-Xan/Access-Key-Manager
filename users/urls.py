from django.contrib import admin
from django.urls import path
from . import views 

app_name = 'users'

urlpatterns = [
    path('login/',views.log_in,name="login"), # path to the login page
    path('signup/',views.signup,name="signup" ), # path to thr sign up page
]