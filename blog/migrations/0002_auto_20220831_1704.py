# Generated by Django 3.2.15 on 2022-08-31 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Single',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Url')),
                ('content', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'single-post',
                'verbose_name_plural': 'single-posts',
                'ordering': ['title'],
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['title'], 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]
