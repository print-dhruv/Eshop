from django.contrib import admin
from store.models import Product, Categories, Customer
# Register your models here.


class AdminProductView(admin.ModelAdmin):
    list_display = ('product_name','product_price','category') #name should be list_display

class AdminCategorieView(admin.ModelAdmin):
    list_display = ('name',)

class AdminCustomerView(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'contact')

admin.site.register(Product, AdminProductView)
admin.site.register(Categories, AdminCategorieView)
admin.site.register(Customer,AdminCustomerView)
