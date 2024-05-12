from django.shortcuts import render,redirect

#this is the inital page for the app,it should redirect to the login page to allow users to login before they can view any content
def home(request):
    if request.method == 'GET':
        return redirect('users:login')