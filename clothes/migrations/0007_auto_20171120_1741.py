# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-20 17:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0006_auto_20171120_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='color',
            field=models.CharField(choices=[('black', 'Black'), ('Blue', 'Blue'), ('brown', 'Brown'), ('grey', 'Grey'), ('navy', 'Navy'), ('red', 'Red'), ('white', 'White'), ('green', 'Green')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='itemGroup',
            field=models.CharField(choices=[('leathershoes', 'Leather Shoes'), ('trainer', 'Trainer'), ('tshirt', 'T-Shirt'), ('poloshirt', 'Polo Shirt'), ('bomber', 'Bomber'), ('windbreaker', 'Windbreaker')], max_length=60, null=True),
        ),
        migrations.DeleteModel(
            name='ItemGroup',
        ),
    ]
