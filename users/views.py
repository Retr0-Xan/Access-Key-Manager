from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout

#this function renders the login page
def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request,form.get_user())
            return render(request,'users/home.html')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form':form})

#this function renders the signup page
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'users/home.html')
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form':form})