# Generated by Django 4.1.4 on 2023-04-21 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_product_name_products_product_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='product',
            new_name='product_name',
        ),
    ]
