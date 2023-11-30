from django.db import models
from django.contrib.auth.hashers import make_password
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    price = models.DecimalField(max_digits=5,decimal_places=2)
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    quantity= models.IntegerField()
    def __str__(self):
        return self.title

class Customer(models.Model):
    name= models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=128)

    def save(self):
        self.password = make_password(self.password)
        super().save()

    def __str__(self):
        return self.name
    
class Order(models.Model):
    book= models.ManyToManyField(Book)
    customer= models.ManyToManyField(Customer)
    quantity = models.IntegerField()
