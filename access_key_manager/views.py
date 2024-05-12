from django.shortcuts import render,redirect

#this function renders the login page
def log_in(request):
    return render(request, 'login.html')

#this function renders the signup page
def signup(request):
    return render(request, 'signup.html')

#this is the inital page for the app,it should redirect to the login page to allow users to login before they can view any content
def home():
    return redirect(log_in)