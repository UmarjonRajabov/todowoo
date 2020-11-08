from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def signupuser(request):
    return render(request,'todo/signupuser.html',{'form': UserCreationForm()})