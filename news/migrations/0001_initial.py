# Generated by Django 3.2.21 on 2023-09-27 17:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=80)),
                ('source_id', models.CharField(max_length=30)),
                ('source_name', models.CharField(max_length=30)),
                ('article_url', models.TextField()),
                ('image_url', models.TextField()),
                ('description', models.TextField()),
                ('date_published', models.DateTimeField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]