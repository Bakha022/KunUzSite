from django.shortcuts import render
from django.views.generic import  ListView, DetailView
from .models import NewsType, RegionalNews
# Create your views here.

class CategoryView(ListView):
    model = NewsType
    template_name = 'home.html'
