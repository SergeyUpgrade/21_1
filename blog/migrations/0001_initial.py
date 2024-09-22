# Generated by Django 5.1.1 on 2024-09-22 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите заголовок', max_length=100, verbose_name='Заголовок')),
                ('slug', models.CharField(max_length=150, verbose_name='slug')),
                ('content', models.TextField(blank=True, help_text='Введите текст', null=True, verbose_name='Содержание')),
                ('image', models.ImageField(blank=True, help_text='Загрузите изображение', null=True, upload_to='catalog/image', verbose_name='Изображение')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('is_published', models.BooleanField(default=True)),
                ('views_count', models.IntegerField(default=0, verbose_name='просмотры')),
            ],
        ),
    ]
