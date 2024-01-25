from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    username = models.CharField(max_length=13, unique=True, blank=False, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='invalid_number'
        ), ])
    phone_model = models.CharField(max_length=255, verbose_name='Model', blank=True, null=True)
    shop_name = models.CharField(max_length=255, blank=True, null=True)
    used_limit = models.BooleanField(default=False)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    limit = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


