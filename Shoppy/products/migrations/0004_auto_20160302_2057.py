# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-02 20:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20160302_1743'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='imagen',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to=b''),
        ),
    ]
