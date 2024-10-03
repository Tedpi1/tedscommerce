from django.contrib import admin
from .models import Customers, Product, Orders, Category

# Register your models here.
admin.site.register(Customers)
admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(Category)