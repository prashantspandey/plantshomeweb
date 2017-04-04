# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-04 20:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstone', '0045_auto_20170405_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='category',
            field=models.CharField(choices=[('Ornamental', 'Ornamental'), ('Herbs', 'Herbs'), ('Shrubs', 'Shrubs'), ('Flowering and Seasonal', 'Flowering and Seasonal'), ('Trees', 'Tree'), ('Palm', 'Palm'), ('Fruits', 'Fruits'), ('Grass', 'Grass'), ('Bonsai', 'Bonsai')], default='Shrubs', max_length=50),
        ),
        migrations.AlterField(
            model_name='plantsize',
            name='size',
            field=models.CharField(choices=[('Thick', 'Thick'), ('Thin', 'Thin'), ('0-2 feet', '0-2 feet'), ('2-4 feet', '2-4 feet'), ('4-6 feet', '4-6 feet'), ('6-8 feet', '6-8 feet'), ('8-10 feet', '8-10 feet'), ('Seedling', 'Seedling')], max_length=100),
        ),
    ]
