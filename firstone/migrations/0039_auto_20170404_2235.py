# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-04 17:05
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstone', '0038_auto_20170404_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(9999999999), django.core.validators.MinLengthValidator(10)]),
        ),
    ]