from rest_framework import serializers ,status
from .models import Book , Order , Customer
class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=6, decimal_places=2)
    quantity = serializers.IntegerField()

    def create(self, data):
        return Book.objects.create(**data)
    
class OrderSerializer(serializers.Serializer):
    
    id = serializers.IntegerField(read_only=True)
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all(), many=True)
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all(), many=True)
    quantity = serializers.IntegerField()

    def create(self, data):
        return Order.objects.create(**data)
    
