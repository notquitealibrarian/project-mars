# Generated by Django 3.2.7 on 2021-12-02 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='New Product', max_length=360)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=100)),
                ('image', models.ImageField(default='default.jpg', upload_to='media')),
                ('part_number', models.CharField(default='X0000000', max_length=360)),
                ('category', models.CharField(choices=[('CT', 'Cervical/Trauma'), ('IFAVBR', 'Interbody Fusion and Vertebral Body Replacement'), ('TC', 'Thoracolumbar'), ('MAST', 'MAST'), ('GI', 'General Instruments')], max_length=6, null=True)),
                ('size', models.CharField(default='Medium', max_length=120)),
                ('handle', models.CharField(choices=[('A', '1.9 Inch Ball w/ Impact Cap'), ('B', '4.8 Inch Ergonomic Inline'), ('C', '4.75 Inch Tapered w/ Impact Cap'), ('D', '6 Inch Ergonomic Inline w/ Impact Cap'), ('E', '4 Inch Cervical Inline w/Impact Cap')], max_length=1, null=True)),
                ('product_type', models.CharField(choices=[('A', 'Simple Modification - Make from Scratch'), ('B', 'Minor Mod to Standard Device'), ('C', 'Complex Design - Requires Predicate'), ('D', 'Complex Assembly - Many Components')], max_length=1, null=True)),
                ('num_orders', models.PositiveIntegerField(default=0)),
                ('department', models.CharField(blank=True, default='', max_length=20)),
            ],
        ),
    ]
