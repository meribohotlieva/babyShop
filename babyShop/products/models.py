from django.db import models

# Create your models here.


class Product(models.Model):
    product_image = models.URLField()
    product_name = models.CharField(max_length=50)
    caption = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

