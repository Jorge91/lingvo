# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 22:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0002_auto_20160518_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='born_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='genre',
            field=models.CharField(blank=True, choices=[(b'MSC', 'Masculine'), (b'FMN', 'Feminine')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=b'profiles'),
        ),
    ]
