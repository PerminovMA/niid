# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-26 21:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('niid_db', '0023_toxchar_subac_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='toxchar',
            name='ac_value',
            field=models.FloatField(blank=True, null=True, verbose_name='\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 Zbioc.eff.ac'),
        ),
        migrations.AlterField(
            model_name='toxchar',
            name='subac_value',
            field=models.FloatField(blank=True, null=True, verbose_name='\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 Zbioc.eff.subac'),
        ),
    ]
