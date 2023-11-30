# Generated by Django 4.2.6 on 2023-10-26 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_remove_order_customer_customer_order_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ManyToManyField(to='products.customer'),
        ),
    ]
