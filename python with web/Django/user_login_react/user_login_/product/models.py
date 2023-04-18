from django.db import models

# Create your models here.


class ProductCategory(models.Model):
    parent_category_id = models.ForeignKey(
        'ProductCategory', null=True, blank=True, on_delete=models.SET_NULL)
    # parent_category_id2 = models.IntegerField()
    category_name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.category_name


class Product(models.Model):
    category_id = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    # product_image = 

# class Product_images(models.Model):
#     images = models.ImageField(upload_to='Product_image/')
#     filedFiled = models.FileField(upload_to='file/')
    
