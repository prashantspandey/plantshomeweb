# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-02 21:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstone', '0016_remove_cart_planter'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='size',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
    ]