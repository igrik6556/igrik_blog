# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-02-26 20:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название тэга')),
                ('slug', models.SlugField(verbose_name='Слаг')),
            ],
            options={
                'verbose_name_plural': 'Тэги',
                'db_table': 'Tag',
                'verbose_name': 'Тэг',
            },
        ),
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='tag', to='my_blog.Tag', verbose_name='Article tag'),
        ),
    ]