# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-27 20:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0013_auto_20171127_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='itemGroup',
            field=models.CharField(choices=[('hoodie', 'Hoodie'), ('boots', 'Boots'), ('top-f', 'Top (F)'), ('boots-f', 'Boots (f)'), ('leatherjacket-f', 'Leather Jacket (f)'), ('skirt-f', 'Skirt (f)'), ('desertboots', 'Desert Boots'), ('sunglasses', 'Sunglasses'), ('sweatshirt', 'Sweatshirt'), ('cap', 'Cap'), ('wovenbelt', 'Woven Belt'), ('boatshoes', 'Boat Shoes'), ('chelsea', 'Chelsea Boots'), ('shoes', 'Shoes'), ('chinos', 'Chinos'), ('leathershoes', 'Leather Shoes'), ('trainers', 'Trainers'), ('tshirt', 'T-Shirt'), ('poloshirt', 'Polo Shirt'), ('bomber', 'Bomber'), ('windbreaker', 'Windbreaker'), ('jeans', 'Jeans'), ('shirt', 'Shirt'), ('belt', 'Belt')], max_length=60),
        ),
        migrations.AlterField(
            model_name='outfit',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=30),
        ),
    ]
