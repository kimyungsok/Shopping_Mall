# Generated by Django 4.0.5 on 2022-06-15 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unisex',
            name='main_photo',
            field=models.ImageField(upload_to=''),
        ),
    ]
