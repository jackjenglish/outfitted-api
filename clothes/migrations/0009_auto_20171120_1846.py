# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-20 18:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0008_auto_20171120_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='srclink',
            field=models.CharField(default='www.default.com', max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='itemGroup',
            field=models.CharField(choices=[('leathershoes', 'Leather Shoes'), ('trainers', 'Trainers'), ('tshirt', 'T-Shirt'), ('poloshirt', 'Polo Shirt'), ('bomber', 'Bomber'), ('windbreaker', 'Windbreaker')], max_length=60),
        ),
    ]
