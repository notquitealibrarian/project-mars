# Generated by Django 3.2.7 on 2021-12-01 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='department',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
