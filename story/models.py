from django.db import models


class StoreAbout(models.Model):
    name = models.CharField(max_length=255, verbose_name='store name')
    plastic_number = models.IntegerField(verbose_name='store plastic number')
    address = models.CharField(max_length=255, verbose_name='store address')


class DebtMarket(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    deadline = models.DateField()
    date = models.DateField()


class Cost(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    extra = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)