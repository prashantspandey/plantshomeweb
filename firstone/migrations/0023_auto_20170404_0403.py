# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-03 22:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstone', '0022_ratingplant_reviewtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
    ]
