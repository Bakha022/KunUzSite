from django.shortcuts import render, get_object_or_404
from django.views.generic import  ListView, DetailView
from .models import NewsType, RegionalNews
# Create your views here.

class CategoryView(ListView):
    model = NewsType
    template_name = 'base.html'



    
def RegionalView(request):
    object_list = NewsType.objects.all()
    one_article = RegionalNews.objects.first()
    four_articels = RegionalNews.objects.order_by('id')[:4]
    theEditor = RegionalNews.objects.order_by('id')[4:7]
    ctx = {
        "four_articels" : four_articels,
        "one_articles": one_article,
        "object_list": object_list,
        "theEditor": theEditor
    }
    return render(request, 'home.html', ctx)


