from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import user

def home(request):
    en=user.objects
    return render(request,'enroll/home.html',{'enr':en})