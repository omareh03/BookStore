from django.contrib import admin
from .models import Product , Book,Customer,Order
# Register your models here.
admin.site.register(Product)
admin.site.register(Book)
admin.site.register(Customer)
admin.site.register(Order)

