# Generated by Django 3.2.7 on 2021-10-07 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20211007_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='handle',
            field=models.CharField(default='None', max_length=360),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='New Product', max_length=360),
        ),
    ]