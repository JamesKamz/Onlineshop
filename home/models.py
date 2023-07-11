from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    name=models.CharField(max_length=255)
    description=models.TextField(blank=True, null=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True, null=True)
    cover_image=models.ImageField(upload_to='images')
    price=models.DecimalField(max_digits=9, decimal_places=2)
    number=models.PositiveIntegerField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE )
    
    def __str__(self):
        return f'Nom : {self.name} || Prix: {self.price} '

class Order(models.Model):
    name=models.CharField(max_length=200)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=500,null=True)
    telephone = models.CharField(max_length=20,null=True)
    order_date= models.DateField(auto_now_add=True,null=True)

class Article(models.Model):
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    name=models.CharField(max_length=255)
    slug=models.SlugField(default=None)
    description=models.TextField()

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    
    def add_product(self, product):
        self.products.add(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_products(self):
        return self.products.all()