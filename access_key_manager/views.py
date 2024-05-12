from django.shortcuts import render,redirect

def log_in(request):
    return render(request, 'login.html')
def signup(request):
    return render(request, 'signup.html')

def home():
    return redirect(log_in)