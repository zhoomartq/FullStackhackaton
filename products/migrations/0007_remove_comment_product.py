# Generated by Django 3.2.4 on 2021-06-25 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='product',
        ),
    ]