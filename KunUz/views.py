from django.shortcuts import render
from django.views.generic import  ListView, DetailView
from .models import NewsType, RegionalNews
# Create your views here.

class CategoryView(ListView):
    model = NewsType
    template_name = 'base.html'



    
def RegionalView(request):
    object_list = NewsType.objects.all()
    one_article = RegionalNews.objects.all()[:1]
    ctx = {
        "one_article": one_article,
        "object_list": object_list,
    }
    return render(request, 'home.html', ctx)


