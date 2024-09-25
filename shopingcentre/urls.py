from .views import login, signup,home,about,contact,shop
from django.urls import path

urlpatterns = [
    path('', home),
    path('signup/', signup),
    path('login/', login),
    path('about/', about),
    path('contact/', contact),
    path('shop/', shop),
]
