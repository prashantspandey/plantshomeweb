# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-04 01:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstone', '0030_remove_order_orderplantid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
    ]
