from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Username or password is incorrect')
    return render(request, 'login.html')

def signup(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            email=form.cleaned_data['email']
            user=authenticate(username=username, password=password, email=email)
            login(request, user)
            messages.success(request, 'Account was created successfully')
            return redirect('/')
    else:
        form=SignUpForm()
    
    return render(request, 'signup.html',{'form':form})

def logout_user(request):
    logout(request)
    return redirect('/')
def home(request):
    return render(request, 'landing_page.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
def shop(request):
    products = Product.objects.all()
    context={
        'products':products
    }
    return render(request, 'shop.html', context)

def product(request, pk):
    product = Product.objects.get(id=pk)
    context={
        'product':product
    }
    return render(request, 'product.html', context)

def category(request, foo):
    foo= foo.replace('-', ' ')
    # grab the category from the url\\
    try:
        # lookup the category
        category=Category.objects.get(name=foo)
        # get all products in that category
        products=Product.objects.filter(category=category)
        return render(request, 'category.html', {'products':products, 'category':category})
    except:
        messages.success(request, 'Category does not exist')
        return redirect('/')