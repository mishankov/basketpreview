# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 09:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170314_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover_link',
            field=models.ImageField(default=0, upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_link',
            field=models.ImageField(default=0, upload_to=''),
        ),
    ]
