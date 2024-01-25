from django.db import models
from category.models import Category


class Product(models.Model):
    product_name = models.CharField(max_length=255, verbose_name='product_name')
    barcodes = models.BigIntegerField(verbose_name='shtrix code', unique=True)
    purchase_price = models.FloatField()
    sel_price = models.FloatField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='product')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
