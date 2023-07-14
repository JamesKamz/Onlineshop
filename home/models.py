from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    name=models.CharField(max_length=255)
    description=models.TextField(blank=True, null=True)
    active=models.BooleanField(default=True)
    
    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    
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
    number=models.PositiveIntegerField(default=1)
    category=models.ForeignKey(Category, on_delete=models.CASCADE )

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter (id__in=ids)
    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter (category=category_id)
        else:
            return Product.get_all_products()
    
    def __str__(self):
        return f'Nom : {self.name} || Prix: {self.price} '

class Pack(models.Model):
    name=models.CharField(max_length=255)
    active=models.BooleanField(default=True)
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    option5=models.CharField(max_length=100)
    validated_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    name=models.CharField(max_length=255)
    slug=models.SlugField(default=None)
    description=models.TextField()

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
    products = models.ManyToManyField(Product)
    
    def placeOrder(self):
        self.save()

    def add_product(self, product):
        self.products.add(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_products(self):
        return self.products.all()
    
class Order(models.Model):
    customer=models.ForeignKey(User, on_delete=models.CASCADE, default=True)
    commaand=models.ForeignKey(Cart,on_delete=models.CASCADE, null=True)
    email = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=500,null=True)
    telephone = models.CharField(max_length=20,null=True)
    order_date= models.DateField(auto_now_add=True)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(user_id):
        return Order.objects.filter(customer=user_id).order_by('-order_date')