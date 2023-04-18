from django.db import models

# Create your models here.


class Product_images(models.Model):
    imageUrl = models.TextField()
    # filedFiled = models.FileField(upload_to='file/')
