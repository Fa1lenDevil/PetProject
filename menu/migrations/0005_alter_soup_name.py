# Generated by Django 4.2.1 on 2023-05-30 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_drinks_image_snack_image_soup_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soup',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
