# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-02 17:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='imagen',
        ),
    ]
