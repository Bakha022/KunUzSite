from django.urls import path
from .views import CategoryView 

urlpatterns = [
    path('', CategoryView, name= 'base.html')
]



