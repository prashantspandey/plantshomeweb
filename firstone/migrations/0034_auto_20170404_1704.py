# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-04 11:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstone', '0033_auto_20170404_0713'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='plids',
            new_name='plnames',
        ),
    ]