# Generated by Django 4.0.5 on 2022-06-30 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_rename_postdetailcontent_postdetail_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='postdetail',
            name='post_name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
