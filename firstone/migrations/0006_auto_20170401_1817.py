# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-01 12:47
from __future__ import unicode_literals

from django.db import migrations, models
import firstone.models


class Migration(migrations.Migration):

    dependencies = [
        ('firstone', '0005_auto_20170401_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='image1',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to=firstone.models.upload_location),
        ),
    ]
