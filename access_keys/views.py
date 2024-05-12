from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/users/login/')
def access_key_list(request):
    return render(request, 'access_keys/home.html')
