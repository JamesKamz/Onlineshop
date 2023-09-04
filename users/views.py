from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from .forms import *


def Userlogin(request):
    if request.method=='POST':
        form=AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else :
                messages.error(request, "Nom d'utilisateur ou mot de passe incorect")
        else :
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect")
    elif request.method=='GET':
        form=AuthenticationForm()
    return render(request, 'login.html', {'form':form})

class UserSignup(CreateView):
    model=User
    form_class=RegisterForm
    template_name='signup.html'

    def form_valid(self, form):
        user=form.save()
        login(self.request, user)
        return redirect('login')
    
def Userlogout(request):
    logout(request)
    return redirect('login')

def Errorview(request, exception):
    return render(request, 'error404.html', status=404)