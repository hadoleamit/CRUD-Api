from django.shortcuts import render
from rest_framework import generics
from .models import *
from my_app.serializers import ProductSerializer

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product
    serializer_class = ProductSerializer