# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-01 19:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstone', '0010_plantprices'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plant',
            name='price',
        ),
    ]
