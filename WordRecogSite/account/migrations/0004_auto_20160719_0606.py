# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-19 06:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_connection'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_picture',
            new_name='photo',
        ),
    ]
