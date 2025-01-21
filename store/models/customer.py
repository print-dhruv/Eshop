from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=50)