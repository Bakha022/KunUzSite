from django.urls import path
from .views import CategoryView 

urlpatterns = [
    path('home/', CategoryView.as_view(), name="base")
]  