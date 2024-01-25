from django.db import models
from django.core.validators import RegexValidator


class Client(models.Model):
    name = models.CharField(max_length=255, verbose_name='client_name')
    phone = models.CharField(max_length=13, unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='invalid_number'
        ), ])
    debt = models.FloatField(null=True, blank=True)
    date = models.DateField(blank=True, null=True)


class Employee(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13, unique=True, blank=False, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='invalid_number'
        ), ])
    password = models.CharField(max_length=255,  null=False, blank=False)

