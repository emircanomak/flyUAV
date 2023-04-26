from django.contrib import admin

from .models import uavModel
# Register your models here.
@admin.register(uavModel)
class uavModelAdmin(admin.ModelAdmin):
    list_display=('name','brand','weight','category','date','image')

    class Meta:
        model=uavModel

    
    