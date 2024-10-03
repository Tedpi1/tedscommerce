from .views import login_user, signup,home,about,contact,shop,logout_user,product, category
from django.urls import path
app_name = 'shopingcentre'
urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup,name='signup'),
    path('login/', login_user,name='login'),
    path('logut/', logout_user,name='logout'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('shop/', shop, name='shop'),
    path('product/<int:pk>', product, name='product'),   
    path('category/<str:foo>', category, name='category'),
]
