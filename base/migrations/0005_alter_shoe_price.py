# Generated by Django 4.1.7 on 2023-03-13 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_shoe_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoe',
            name='price',
            field=models.IntegerField(max_length=10),
        ),
    ]