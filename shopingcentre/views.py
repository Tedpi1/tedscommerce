from django.shortcuts import render

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def home(request):
    return render(request, 'landing_page.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
def shop(request):
    return render(request, 'shop.html')
# Create your views here.
