# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-11-28 11:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IDF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=10, verbose_name='tag')),
                ('IDF', models.IntegerField(verbose_name='IDF')),
                ('CATE', models.IntegerField(verbose_name='CATE')),
            ],
        ),
        migrations.CreateModel(
            name='ISBN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISBN', models.IntegerField(verbose_name='ISBN')),
                ('RFS', models.IntegerField(verbose_name='RFS')),
                ('tag', models.CharField(max_length=10, verbose_name='tag')),
                ('TF', models.IntegerField(verbose_name='TF')),
                ('CATE', models.IntegerField(verbose_name='CATE')),
            ],
        ),
    ]
