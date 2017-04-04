# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-04 01:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstone', '0031_remove_order_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='firstone.Cart'),
            preserve_default=False,
        ),
    ]
