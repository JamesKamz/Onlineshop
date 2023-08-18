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

class AdminPack(admin.ModelAdmin):
    list_display=('name', 'option1', 'option2', 'option3', 'option4', 'option5', 'validated_date')


admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategorie)
admin.site.register(Article, AdminArticle)
admin.site.register(Order, AdminOrder)
admin.site.register(Pack, AdminPack)