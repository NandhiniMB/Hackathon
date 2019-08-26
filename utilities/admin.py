from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Utilities,Utility_Category
# from mapwidgets.widgets import GooglePointFieldWidget


@admin.register(Utilities)
class UtilitiesAdmin(OSMGeoAdmin):
    list_display = ('name', 'location','address','city')
    
@admin.register(Utility_Category)
class Utility_CategoryAdmin(OSMGeoAdmin):
    list_display = ('name',)



# Register your models here.
