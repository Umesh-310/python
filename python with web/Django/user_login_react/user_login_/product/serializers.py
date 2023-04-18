from rest_framework import serializers
from .models import ProductCategory, Product


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"


# class ProductCategoryAllSerializer(serializers.ModelSerializer, serializers.Serializer):
#     category = serializers.SerializerMethodField()
#     parent_category = serializers.SerializerMethodField()

#     class Meta:
#         model = Product
#         fields = ('category', 'parent_category',)

#     def get_category(self, obj):
#         category = ProductCategory.objects.filter(parent_category_id=None)
#         return ProductCategorySerializer(category, many=True).data

#     def get_parent_category(self, obj):
#         parent_category = ProductCategory.objects.all().filter(
#             parent_category_id=13)
#         return ProductCategorySerializer(parent_category, many=True).data
