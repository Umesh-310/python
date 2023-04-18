from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, Listing, Image, Message, Transaction, Review


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class ListingSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    seller = UserSerializer(read_only=True)
    images = serializers.SerializerMethodField()

    class Meta:
        model = Listing
        fields = ('id', 'title', 'description', 'price',
                  'location', 'category', 'seller', 'images')

    def get_images(self, obj):
        images = Image.objects.filter(listing=obj)
        return ImageSerializer(images, many=True).data


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'image')


class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    receiver = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ('id', 'content', 'sender', 'receiver', 'timestamp')


class TransactionSerializer(serializers.ModelSerializer):
    buyer = UserSerializer(read_only=True)
    seller = UserSerializer(read_only=True)
    item = ListingSerializer(read_only=True)

    class Meta:
        model = Transaction
        fields = ('id', 'buyer', 'seller', 'item', 'amount')


class ReviewSerializer(serializers.ModelSerializer):
    reviewer = UserSerializer(read_only=True)
    reviewee = UserSerializer(read_only=True)
    transaction = TransactionSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'content', 'rating',
                  'reviewer', 'reviewee', 'transaction')
