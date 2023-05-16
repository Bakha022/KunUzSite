from django.contrib import admin
from .models import NewsType, RegionalNews

# Register your models here.
# class SuperAdmin(admin.ModelAdmin):
#     filter_horizontal = ('NewstType', 'RegionalNews')


admin.site.register(NewsType)
admin.site.register(RegionalNews)
