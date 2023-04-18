from django.db import models
from django.contrib.auth.models import User

import uuid
from django.utils import timezone

# Create your models here.

# class Details(models.Model):
#     details = models.ManyToManyField()


class AddProduct(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    product_title = models.CharField(max_length=200)
    product_image1 = models.ImageField()
    product_image2 = models.ImageField(null=True, blank=True)
    product_image3 = models.ImageField(null=True, blank=True)
    product_image4 = models.ImageField(null=True, blank=True)
    product_image5 = models.ImageField(null=True, blank=True)
    product_description = models.TextField()
    product_price = models.IntegerField()
    product_buying_cost = models.IntegerField()
    product_address = models.TextField()
    product_category = models.CharField(
        max_length=100, null=False, blank=False)
    is_create = models.DateField(default=timezone.now)
    owner = models.ForeignKey(
        User, related_name="owner", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.product_title}"


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Listing(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    location = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title




class Message(models.Model):
    content = models.TextField()
    sender = models.ForeignKey(
        User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(
        User, related_name='received_messages', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


class Transaction(models.Model):
    buyer = models.ForeignKey(
        User, related_name='transactions_as_buyer', on_delete=models.CASCADE)
    seller = models.ForeignKey(
        User, related_name='transactions_as_seller', on_delete=models.CASCADE)
    item = models.ForeignKey(Listing, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)


class Review(models.Model):
    content = models.TextField()
    rating = models.PositiveSmallIntegerField()
    reviewer = models.ForeignKey(
        User, related_name='reviews_as_reviewer', on_delete=models.CASCADE)
    reviewee = models.ForeignKey(
        User, related_name='reviews_as_reviewee', on_delete=models.CASCADE)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
