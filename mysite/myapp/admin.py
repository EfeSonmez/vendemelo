from django.contrib import admin
from .models import Product
# Register your models here.



admin.site.site_header = "vendemelo Controlling Panel"

admin.site.site_title = "vendemelo app"

admin.site.index_title = "vendemelo Site Administration"

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','desc')
    search_fields = ['name']
    
    
admin.site.register(Product, ProductAdmin)