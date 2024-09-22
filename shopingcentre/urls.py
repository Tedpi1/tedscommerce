from .views import login, signup,home,about
from django.urls import path

urlpatterns = [
    path('', home),
    path('signup/', signup),
    path('login/', login),
    path('about/', about),
]
