# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-11 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0003_auto_20160520_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=b'pictures'),
        ),
    ]
