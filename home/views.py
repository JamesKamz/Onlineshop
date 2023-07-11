from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView
from home.forms import ContactusForm
from home.models import *
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse



@login_required
def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = Product.objects.get(pk=product_id)
        
        cart = request.user.cart  # Assuming you have a OneToOneField relationship from User to Cart
        cart.add_product(product)
        
        return JsonResponse({'success': True})
    
    return JsonResponse({'success': False})

@login_required
def view_cart(request):
    cart = request.user.cart
    cart_products = cart.get_products()
    activate_page='view_cart'
    context = {
        'cart_products': cart_products,
        'activate_page': activate_page
    }
    return render(request, 'cart.html', context)


def home(request):
    products=Product.objects.all().order_by('name')
    item_name=request.GET.get('item-name')
    activate_page='home'
    if item_name !='' and item_name is not None:
        products=Product.objects.filter(name__icontains=item_name)
    
    paginator=Paginator(products, 4)
    page=request.GET.get('page')
    products=paginator.get_page(page)
    return render(request, 'home.html', {'products': products, 'activate_page': activate_page})

def detail(request, id):
    product=Product.objects.get(pk=id)
    return render(request, 'detail.html', {'product':product})

def CategoryViewset(request):
    activate_page='category'
    categories=Category.objects.all()
    return render(request, 'category.html', {'categories':categories, 'activate_page':activate_page})

def categorydetail(request, id):
    categor=Category.objects.get(pk=id)
    products=Product.objects.filter(category=categor)
    return render(request, 'categorydetail.html', {'category':categor, 'products':products})

def ProductViewset(request):
   products=Product.objects.all()
   item_name=request.GET.get('item-name')
   activate_page='product'
   if item_name !='' and item_name is not None:
        products=Product.objects.filter(name__icontains=item_name)
   return render(request, 'products.html', {'products': products, 'activate_page':activate_page})
   
    
class ArticleViewset(ListView):
    model=Article
    template_name='blog.html'
    context_object_name='articles'
    
    

def AboutusView(request):
    activate_page='about'
    return render(request,'aboutus.html', {'activate_page':activate_page},)

def ContactusView(request):
    sub = ContactusForm()
    activate_page='contact'
    if request.method == 'POST':
        sub = ContactusForm(request.POST)
    return render(request, 'contactus.html', {'form':sub, 'activate_page':activate_page},)

