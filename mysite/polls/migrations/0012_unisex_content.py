# Generated by Django 4.0.5 on 2022-06-30 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_postdetail_post_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='unisex',
            name='content',
            field=models.TextField(null=True),
        ),
    ]
