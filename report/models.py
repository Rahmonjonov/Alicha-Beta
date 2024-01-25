from django.db import models
from products.models import Product
from person.models import Client


class Order(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, blank=True, null=True)


class Checkout(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(blank=True, null=True)
    deadline = models.DateField(null=True)
    date_now = models.DateField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.PROTECT, blank=True, null=True)
    order = models.ManyToManyField(to=Order)
    PAYMENT_CHOICES = (

        (0, "Naqd"),
        (1, "Qarz"),
        (2, "Plastik"),
    )
    type_payment = models.IntegerField(default=0, choices=PAYMENT_CHOICES)
