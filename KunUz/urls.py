from django.urls import path
from .views import CategoryView , RegionalView

urlpatterns = [
    path('base/', CategoryView.as_view(), name="base"),
    path('home/', RegionalView, name="home")
] 


