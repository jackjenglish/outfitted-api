# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-20 18:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0010_auto_20171120_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='size',
            field=models.ManyToManyField(blank=True, null=True, to='clothes.ItemSize'),
        ),
    ]
