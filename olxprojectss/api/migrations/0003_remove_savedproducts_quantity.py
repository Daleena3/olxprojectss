# Generated by Django 4.1.4 on 2023-04-20 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_savedproducts_qty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='savedproducts',
            name='quantity',
        ),
    ]