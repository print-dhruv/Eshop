import datetime
from django.db import models
from .customer import Customer
from .product import Product


class Orders(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=400,blank=False,default="Default Address")
    phone = models.CharField(max_length=15,blank=False,default="0000")
    date = models.DateField(default=datetime.datetime.today)
    status= models.BooleanField(default=False)
