# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-20 14:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0005_auto_20171120_1427'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemgroup',
            old_name='title',
            new_name='name',
        ),
    ]
