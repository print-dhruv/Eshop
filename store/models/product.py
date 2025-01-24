from django.db import models
from .categories import Categories

# Create your models here.
class Product(models.Model):
    product_name= models.CharField(max_length=100)
    product_price= models.IntegerField(default=0)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, default=1)
    product_image = models.ImageField(upload_to='media/')
    product_quantity = models.IntegerField(default=0)
