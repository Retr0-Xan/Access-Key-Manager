from django.contrib import admin
from django.urls import path
from . import views 

app_name = 'access_keys'

urlpatterns = [
    path('',views.home,name="list"), # path to the login page
]