# Generated by Django 4.0.5 on 2022-06-19 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_alter_commentformmodel_recomment_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentformmodel',
            name='recomment_content',
            field=models.CharField(blank=True, help_text='댓글 작성중입니다...', max_length=30),
        ),
        migrations.AlterField(
            model_name='commentformmodel',
            name='recomment_title',
            field=models.CharField(blank=True, help_text='댓글 작성중입니다...', max_length=30),
        ),
    ]
