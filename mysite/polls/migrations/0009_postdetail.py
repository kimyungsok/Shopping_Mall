# Generated by Django 4.0.5 on 2022-06-30 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_alter_commentformmodel_recomment_content_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_photo', models.ImageField(upload_to='PostDetailPhoto/')),
                ('PostDetailContent', models.TextField()),
            ],
        ),
    ]
