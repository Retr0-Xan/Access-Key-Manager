from django.shortcuts import render

#this function renders the login page
def log_in(request):
    return render(request, 'users/login.html')

#this function renders the signup page
def signup(request):
    return render(request, 'users/signup.html')