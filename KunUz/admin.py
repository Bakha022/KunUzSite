from django.contrib import admin
from .models import NewsType, RegionalNews

# Register your models here.

admin.site.register(NewsType)
admin.site.register(RegionalNews)
