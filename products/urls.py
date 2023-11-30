from django.urls import path
from . import views

urlpatterns = [
    path('product', views.product, name='product'),
    path('', views.products, name='products'),
    path('getAllBooks/', views.getAllBooks, name='getAllBooks'),
    path('createOrder/', views.createOrder, name='createOrder'),
    path('createBook/', views.createBook,name='createBook')

]
