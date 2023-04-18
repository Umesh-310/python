from django.db import models

# Create your models here.


class Product_images(models.Model):
    images = models.ImageField(upload_to='Product_imag')
    # filedFiled = models.FileField(upload_to='file/')
