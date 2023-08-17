from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views.generic import ListView, View
from home.forms import ContactusForm
from home.models import *
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404


@csrf_exempt
@login_required(login_url='login')
def add_to_cart(request, product_id):
    if request.method == 'POST':
        # product_id_ = request.POST.get('product_id')
        product = get_object_or_404(Product, pk=product_id)

        cart= Cart.objects.get_or_create(user=request.user)

        cart.products.add(product)

        context={
            'product':product,
            'cart_product': cart.products.values_list('id', flat=True)
        }
        return render (request, 'product.html', context)
    
    return JsonResponse({'success': False, 'message': 'Invalid request'})

@login_required(login_url='login')
def add_item_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart, _= Cart.objects.get_or_create(user=request.user)
    cart.products.add(product)
    
    context={
        'product':product,
        'cart_product': cart.products.values_list('id', flat=True)
    }
    return redirect ('/product/')

@login_required(login_url='login')
def remove_item_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    cart, _= Cart.objects.get_or_create(user=request.user)

    cart.products.remove(product)

    context={
        'product':product,
        'cart_product': cart.products.values_list('id', flat=True)
    }
    return redirect ('/cart/')


@login_required(login_url='login')
def view_cart(request):
    try:
        cart = request.user.cart
        cart_products = cart.get_products()
        cart_total = cart_products.aggregate(total_price=models.Sum('price'))['total_price']
        activate_page = 'view_cart'
        context = {
        'cart_products': cart_products,
        'cart_total': cart_total,
        'activate_page': activate_page
    }
    except Cart.DoesNotExist:
        cart_products = []
        context = {
            'cart_products': cart_products,
            'activate_page': 'view_cart',
            'message': 'Your cart is empty.'
        }
    return render(request, 'cart.html', context)

class OrderView(View):
    def get(self , request ):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request , 'account/orders.html'  , {'orders' : orders})

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
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products()
    
    if item_name !='' and item_name is not None:
        products=Product.objects.filter(name__icontains=item_name)
    data = {}
    data['products'] = products
    data['categories'] = categories
    data['activate_page'] = activate_page
    print('you are : ', request.session.get('username'))
    return render(request, 'products.html', data)
       
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

