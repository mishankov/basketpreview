# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 09:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170311_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cover_link',
            field=models.TextField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='image_link',
            field=models.TextField(default=0),
        ),
    ]