from django.contrib import admin
from .models import*


class AdminCategorie(admin.ModelAdmin):
    list_display=('name', 'date_created')

class AdminProduct(admin.ModelAdmin):
    list_display=('name', 'category', 'price', 'number','date_created')

class AdminArticle(admin.ModelAdmin):
    list_display=('name', 'date_created')

class AdminOrder(admin.ModelAdmin):
    list_display=('customer', 'email', )


admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategorie)
admin.site.register(Article, AdminArticle)
admin.site.register(Order, AdminOrder)