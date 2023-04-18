from rest_framework import serializers
from .models import Product_images


class ImagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product_images
        fields = '__all__'
