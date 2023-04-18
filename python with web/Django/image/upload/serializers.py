from rest_framework import serializers
from .models import Product_images


class ImagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product_images
        fields = '__all__'

    # def to_representation(self, instance):
    #     ret = super().to_representation(instance)
    #     ret['images'] = self.context['request'].build_absolute_uri(ret['images'])
    #     return ret
