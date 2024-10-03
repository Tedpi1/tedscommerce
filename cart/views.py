from django.shortcuts import render, get_object_or_404,redirect
from .models import Cart, CartItem
from shopingcentre.models import Product
from django.http import HttpResponse

def cart_summary(request):
    return render(request, 'cart_summary.html')

# handling session
def _cart_id(request): #create session, hyphen is for private method
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart
def cart_add(request, product_id):
    product=Product.objects.get(id=product_id) #get the block
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request)) #get the cart using the cart id present in the session
    except Cart.DoesNotExist:
        cart=Cart.objects.create(
            cart_id=_cart_id(request)
        ) #if cart does not exist create a new cart
    cart.save()
    
    try:
        cart_item=CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item=CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart
        )
        cart_item.save()
    return HttpResponse(cart_item.product)
    exit()
        #redirect user to cart
    return redirect('cart_summary')
def cart_delete(request):
    return render(request, 'cart_remove.html')
def cart_update(request):
    return render(request, 'cart_update.html')