# Generated by Django 3.2.7 on 2021-10-07 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='handle',
            field=models.TextField(default='None'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.CharField(default='Regular', max_length=120),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(default='Medium', max_length=120),
        ),
    ]