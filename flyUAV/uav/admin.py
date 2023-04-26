from django.contrib import admin

from .models import ihaModel,Category,Brand,Model

# Register your models here.
@admin.register(Category)
class uavModelAdmin(admin.ModelAdmin):
    list_display=('name',)
    class Meta:
        model=Category

@admin.register(Brand)
class uavModelAdmin(admin.ModelAdmin):
    list_display=('name',)
    class Meta:
        model=Brand
@admin.register(Model)
class uavModelAdmin(admin.ModelAdmin):
    list_display=('name',)
    class Meta:
        model=Model
@admin.register(ihaModel)
class uavModelAdmin(admin.ModelAdmin):
    list_display=('model','brand','weight','category','date','image')
    class Meta:
        model=ihaModel

    
    