from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)


class Listing(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)


class Image(models.Model):
    url = models.URLField()
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)


class Message(models.Model):
    content = models.TextField()
    sender = models.ForeignKey(
        User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(
        User, related_name='received_messages', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


class Transaction(models.Model):
    buyer = models.ForeignKey(
        User, related_name='buyer_transactions', on_delete=models.CASCADE)
    seller = models.ForeignKey(
        User, related_name='seller_transactions', on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)


class Review(models.Model):
    content = models.TextField()
    rating = models.IntegerField()
    reviewer = models.ForeignKey(
        User, related_name='given_reviews', on_delete=models.CASCADE)
    reviewee = models.ForeignKey(
        User, related_name='received_reviews', on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
