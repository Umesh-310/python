from rest_framework import serializers
from user_app.models import UserAdd, UserDetails
from app_data.models import AddProduct, User
from app_data.serializers import RegisterSerializer, ProductSerializer, UserDetailsSerializer, UserAddSerializer


class UserWithAllInfoSerializers(serializers.ModelSerializer):
    user = RegisterSerializer(many=False)
    user_address = UserAddSerializer(many=False)
    user_products = serializers.SerializerMethodField()

    def get_user_products(self, user_products):
        userp = AddProduct.objects.filter(owner__username='Aku')

        serializer = ProductSerializer(instance=userp, many=True)
        return serializer.data

    class Meta:
        model = UserDetails
        fields = "__all__"


"""



"""
