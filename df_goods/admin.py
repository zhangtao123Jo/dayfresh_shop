from django.contrib import admin
from .models import TypeInfo,GoodsInfo
# Register your models here.
class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ["id","ttitle"]

class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ["id","gtitle","gprice","gunit","gkucun","gtype","gclick"]

admin.site.register(TypeInfo,TypeInfoAdmin)
admin.site.register(GoodsInfo,GoodsInfoAdmin)
