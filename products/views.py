from django.shortcuts import render
from django.http import JsonResponse
from .models import Product, Book, Customer,Order
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_protect
from .serializer import BookSerializer, OrderSerializer , status
from rest_framework.response import Response


# Create your views here.

def responseData(data):
    data = { "data": [data]}
    message = {"message":"done"}
    data.update(message)
    s = {"status":200}
    data.update(s)
    return data

def product(request):
    return render(request, 'products/product.html')


def products(request):
    return render(request, 'products/products.html', {'pro': Product.objects.all()})

@api_view(['GET'])
def getAllBooks(request):
    books = Book.objects.all()
    serializer = BookSerializer(books,many=True)
    data = responseData(serializer.data)
    return Response(data , status=status.HTTP_200_OK)

def createBookIsValid(data):
    title=data["title"]
    author=data["author"]
    price=data["price"]
    quantity=data["quantity"]
    if isinstance(title,str) and isinstance(author,str) and isinstance(price,float) and isinstance(quantity,int):
        return True
    else: return False


@api_view(['POST'])
def createBook(request):
    serializer = BookSerializer(data=request.data)
    isValid = createBookIsValid(request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    data = responseData(serializer.data)
    return Response(data , status=status.HTTP_200_OK)
   # else:
       # return Response({"Message": "400 Bad Request"},status=status.HTTP_400_BAD_REQUEST)

def is_int_list(val):
    if len(val) == 0:
        return False
    return all(isinstance(x, int) for x in val)

def createOrderIsValid(data):
    book=data["book"]
    customer=data["customer"]
    quantity=data["quantity"]
    if isinstance(book,int) or isinstance(customer,int):
        return False
    if len(book) ==1 and is_int_list(book) and len(customer)==1 and is_int_list(customer) and isinstance(quantity,int):
        return True
    else: return False


@api_view(['POST'])
def createOrder(request):
    serializer = OrderSerializer(data=request.data)
    isValid = createOrderIsValid(request.data)
    if serializer.is_valid() and isValid==True:
        # Create the order object without many-to-many relationships
        order_data = {
            'quantity': serializer.validated_data['quantity']
        }
        order = Order.objects.create(**order_data)

        # Add books to the order
        book_ids = request.data.get('book', [])
        for book_id in book_ids:
            try:
                book = Book.objects.get(pk=book_id)
                order.book.add(book)
            except Book.DoesNotExist:
                # Handle the case where the book doesn't exist
                pass

        # Add customers to the order
        customer_ids = request.data.get('customer', [])
        for customer_id in customer_ids:
            try:
                customer = Customer.objects.get(pk=customer_id)
                order.customer.add(customer)
            except Customer.DoesNotExist:
                # Handle the case where the customer doesn't exist
                pass
        data = responseData(serializer.data)        
        return Response(data)
    else:
        return Response({"Message": "400 Bad Request"},status=status.HTTP_400_BAD_REQUEST)