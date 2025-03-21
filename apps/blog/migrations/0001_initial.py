# Generated by Django 5.1.7 on 2025-03-20 06:21

import ckeditor_uploader.fields
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.CharField(max_length=200)),
                ('title_en', models.CharField(max_length=200)),
                ('title_ru', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique_for_date='publish')),
                ('preview', models.ImageField(upload_to='post/')),
                ('content_uz', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('content_en', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('content_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ('-publish',),
            },
        ),
    ]
