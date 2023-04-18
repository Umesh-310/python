from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, JSONParser
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from .serializers import ImagesSerializers, Product_images

import cloudinary.uploader

# @api_view(["POST"])
# def ImageUpload(request):
#     print(request.data["images"])
#     return Response({"id" : "id"})


class ImageUpload(ListCreateAPIView):
    queryset = Product_images.objects.all()
    serializer_class = ImagesSerializers
    parser_classes = (
        MultiPartParser,
        JSONParser,
    )

    def post(self, request, *args, **kwargs):
        serializer = ImagesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"id": "fail"})


class UploadView(APIView):
    parser_classes = (
        MultiPartParser,
        JSONParser,
    )

    @staticmethod
    def post(request):
        
        file = request.data
        for f in file:
            print(f['images'])
        # upload_data = cloudinary.uploader.upload(file)
        # data = {
        #     "imageUrl": upload_data['secure_url']
        # }
        # serializer = ImagesSerializers(data=data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # else:
        return Response({"id": "fail"})
