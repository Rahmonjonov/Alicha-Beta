from django.db import models


class Category(models.Model):
    image = models.ImageField(upload_to='category', blank=True, null=True)
    name = models.CharField(max_length=255, verbose_name='category name')