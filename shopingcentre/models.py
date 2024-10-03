from django.db import models
import datetime

class Category(models.Model):
    name = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name
class Customers(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone= models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    
    def __str__(self):
        return self.first_name

# all of our Product

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    #add sell staff
    is_sale=models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    def __str__(self):
        return self.name
# customer orders
class Orders(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    address= models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=20, default='', null=True, blank=True)
    date_ordered = models.DateTimeField(default=datetime.datetime.now)
    status= models.CharField(default=False, max_length=20)
    def __str__(self):
        return str(self.id)

