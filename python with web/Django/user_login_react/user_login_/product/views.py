from django.shortcuts import render
from .models import ProductCategory, Product
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .serializers import ProductCategorySerializer
# Create your views here.


class GetCategory(ListAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
