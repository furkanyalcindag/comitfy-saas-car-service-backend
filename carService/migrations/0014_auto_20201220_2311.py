# Generated by Django 3.1.1 on 2020-12-20 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carService', '0013_auto_20201219_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceproduct',
            name='productNetPrice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='serviceproduct',
            name='productTaxRate',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='serviceproduct',
            name='productTotalPrice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]