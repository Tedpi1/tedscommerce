from django.shortcuts import render,redirect, get_object_or_404
from .models import Cart, CartItem#import get_object_or_40    
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from shopingcentre.models import Product
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
def _cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart

@login_required(login_url='shopingcentre:login')
def add_cart(request, product_id):
    product =Product.objects.get(id=product_id)
    try:
        cart= Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(cart_id=_cart_id(request))
    cart.save()
    #putting the product into cart
    try:
        cart_item=CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity +=1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item=CartItem.objects.create(product=product, cart=cart, quantity=1)
        cart_item.save()
    return redirect('cart')

@login_required(login_url='shopingcentre:login')
def remove_cart(request, product_id):
    cart=Cart.objects.get(cart_id=_cart_id(request))
    product=get_object_or_404(Product, id=product_id)
    cart_item=CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -=1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

@login_required(login_url='shopingcentre:login')
def remove_cart_item(request, product_id):
    cart=Cart.objects.get(cart_id=_cart_id(request))
    product=get_object_or_404(Product, id=product_id)
    cart_item=CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart')

@login_required(login_url='shopingcentre:login')
def cart(request, total=0, quantity=0, cart_items=None, tax=0, grand_total=0):
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
        cart_items=CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax=(5 * total)/100
        grand_total=total+tax
    except ObjectDoesNotExist:
        pass
    context={
        'total':total,
        'quantity':quantity,
        'cart_items':cart_items,
        'tax'       :tax,
        'grand_total':grand_total
    }
    return render(request, 'cart_summary.html', context)