# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-20 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0004_auto_20171120_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='size',
            field=models.ManyToManyField(to='clothes.ItemSize'),
        ),
    ]
