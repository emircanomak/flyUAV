from django.contrib import admin

from .models import uavModel
# Register your models here.
@admin.register(uavModel)
class uavModelAdmin(admin.ModelAdmin):
    fields=('name','brand','weight','category','date')


    
    