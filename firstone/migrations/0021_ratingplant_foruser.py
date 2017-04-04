# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-03 01:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('firstone', '0020_auto_20170403_0643'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratingplant',
            name='foruser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
