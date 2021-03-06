# Generated by Django 3.2.7 on 2021-12-02 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_order_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='instrument_category',
            field=models.CharField(choices=[('CT', 'Cervical/Trauma'), ('IFAVBR', 'Interbody Fusion and Vertebral Body Replacement'), ('TC', 'Thoracolumbar'), ('MAST', 'MAST'), ('GI', 'General Instruments'), ('NP', 'New Product')], max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='instrument_handle',
            field=models.CharField(choices=[('A', '1.9 Inch Ball w/ Impact Cap'), ('B', '4.8 Inch Ergonomic Inline'), ('C', '4.75 Inch Tapered w/ Impact Cap'), ('D', '6 Inch Ergonomic Inline w/ Impact Cap'), ('E', '4 Inch Cervical Inline w/Impact Cap'), ('NP', 'New Product'), ('NA', 'Not Applicable')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='instrument_type',
            field=models.CharField(choices=[('A', 'Simple Modification - Make from Scratch'), ('B', 'Minor Mod to Standard Device'), ('C', 'Complex Design - Requires Predicate'), ('D', 'Complex Assembly - Many Components'), ('NP', 'New Product')], max_length=2, null=True),
        ),
    ]
