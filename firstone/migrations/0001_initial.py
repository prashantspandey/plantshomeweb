# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-31 21:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('scientific_name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('In', 'Indoor'), ('Out', 'Outdoor')], default='Out', max_length=50)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('image1', models.FileField(max_length=500, upload_to='')),
                ('image2', models.FileField(max_length=500, upload_to='')),
                ('image3', models.FileField(max_length=500, upload_to='')),
                ('image4', models.FileField(max_length=500, upload_to='')),
            ],
        ),
    ]
