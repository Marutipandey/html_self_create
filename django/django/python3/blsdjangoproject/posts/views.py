from django.shortcuts import render
from django.views.generic import ListView,CreateView
from django.urls import reverse_lazy
from .forms import PostForm
from .models import post
# Create your views here.
class HomePageView(ListView):
    model=post
    template_name='home.html'


class CreatePostView(CreateView):
    model=post
    form_class=PostForm
    template_name='post.html'
    success_url=reverse_lazy('home')

