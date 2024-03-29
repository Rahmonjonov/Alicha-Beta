# Generated by Django 5.0.1 on 2024-01-24 09:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255, verbose_name='product_name')),
                ('barcodes', models.BigIntegerField(unique=True, verbose_name='shtrix code')),
                ('purchase_price', models.FloatField()),
                ('sel_price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('image', models.ImageField(upload_to='product')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='category.category')),
            ],
        ),
    ]
