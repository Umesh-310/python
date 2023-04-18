from django.shortcuts import render
from .models import AddProduct, User
from user_app.models import UserAdd, UserDetails
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer, UserAddSerializer, UserDetailsSerializer
from django.views.generic import CreateView
from user_app.serializers import UserWithAllInfoSerializers

# Create your views here.


@api_view(['GET'])
def allData(request):
    # allprodeuct = AddProduct.objects.filter(owner__username='Aku')
    allprodeuct = AddProduct.objects.all()
    serializer = ProductSerializer(allprodeuct, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def allUser(request):
    allprodeuct = UserDetails.objects.all()
    # allproduct = UserDetails.objects.get(
    #     id='f794539f-c0aa-44dd-a96a-733aeff53d2c')
    # serializer = UserWithAllInfoSerializers(allproduct, many=False)
    serializer = UserWithAllInfoSerializers(allprodeuct, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addProduct(request):
    addpro = AddProduct()
    addpro.product_title = request.data['product_title']
    addpro.product_image1 = request.data['product_image1']
    addpro.product_description = request.data['product_description']
    addpro.product_price = request.data['product_price']
    addpro.product_buying_cost = request.data['product_buying_cost']
    addpro.product_address = request.data['product_address']
    addpro.product_category = request.data['product_category']
    addpro.owner = UserAdd.objects.get(id=request.data['owner'])
    addpro.save()
    return Response(request.data)


class ProductCreate(CreateView):
    model = AddProduct
    fields = '__all__'
    success_url = ''


class UserCreate(CreateView):
    model = UserDetails
    fields = '__all__'
    success_url = ''


class UserAddCreate(CreateView):
    model = UserAdd
    fields = '__all__'
    success_url = ''
