# from .serializers import CategorySerializer
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework import permissions
from .models import Category, User, Listing, Image, Message, Transaction, Review
from .serializers import CategorySerializer, ListingSerializer, ImageSerializer, MessageSerializer, TransactionSerializer, ReviewSerializer


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]


class ListingList(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [permissions.AllowAny]


class ListingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [permissions.AllowAny]


class ImageList(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.AllowAny]


class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.AllowAny]


class MessageList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.AllowAny]


class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.AllowAny]


class TransactionList(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.AllowAny]


class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.AllowAny]


class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]


class CategoryCreate(generics.CreateAPIView):
    serializer_class = CategorySerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListingCreate(generics.CreateAPIView):
    serializer_class = ListingSerializer

    def post(self, request, *args, **kwargs):
        pk = request.data['category']
        print({"hello" : pk})
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.category = Category.objects.get(id=request.data['category'])
            serializer.seller = User.objects.get(
                id=request.data['seller'])
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
To create URLs for the other models in your Django application, you can define
similar URL patterns that map to their corresponding views. You can also use named
URL patterns to make it easier to refer to them in your code. For example:


urlpatterns = [
    path('categories/create/', CategoryCreate.as_view(), name='category-create'),
    path('listings/create/', ListingCreate.as_view(), name='listing-create'),
    path('users/create/', UserCreate.as_view(), name='user-create'),
    # ...
]


"""
