from django.db import models
from django.contrib.auth.models import User


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


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
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
