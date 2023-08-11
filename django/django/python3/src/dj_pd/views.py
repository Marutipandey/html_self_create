from enum import auto
from  django.shortcuts import render,redirect
from httplib2 import Authentication
from .forms import LoginForm
from django.contrib.auth import  authenticate,login,logout

from dj_pd.forms import LoginForm

def home_view(request):
    return render(request,'home.html',{})

def logout_view(request):
    logout(request)
    return redirect('home')

def login_view(request):
    error_message = None
    form=LoginForm()
    if request.method == 'POST':
        form=LoginForm(data=request.POST)
        if form.is_valid():
            username=form.data.get('username')
            password=form.data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                else:
                    return redirect('home')

            else:
                error_message='UPs.Something went wrong...'
        print(form.data)
    return render(request,'login.html',{'form':form,'error_message':error_message})