# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-08 21:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20160302_2057'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',)},
        ),
    ]
