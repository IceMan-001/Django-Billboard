# Generated by Django 5.1.1 on 2024-09-30 19:16

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
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('text', models.TextField(max_length=500, verbose_name='Текст объявления')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Опубликовано')),
                ('url_adders', models.CharField(max_length=150, verbose_name='Ссылка на сайт')),
                ('image', models.ImageField(null=True, upload_to='posts/', verbose_name='Изображение')),
                ('slug', models.SlugField(editable=False, max_length=200, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
            },
        ),
    ]
