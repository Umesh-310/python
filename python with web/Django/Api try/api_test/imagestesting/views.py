from django.shortcuts import render
# from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ImagesSerializers, Product_images
# Create your views here.


class ImageFile(APIView):
    # queryset = Product_images.objects.all()
    # serializer_class = ImagesSerializers

    def post(self, request):
        print(request.data["images"])
        return Response({"dad": "request.data["'images'"]"})
        # return Response({"dad": request.data["images"]})
