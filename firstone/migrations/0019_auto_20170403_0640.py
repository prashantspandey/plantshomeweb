# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-03 01:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstone', '0018_cart_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='photo',
            field=models.URLField(blank=True, null=True),
        ),
    ]