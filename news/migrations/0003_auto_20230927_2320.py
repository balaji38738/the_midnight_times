# Generated by Django 3.2.21 on 2023-09-27 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_article_source_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_url',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='date_published',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='image_url',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='source_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]