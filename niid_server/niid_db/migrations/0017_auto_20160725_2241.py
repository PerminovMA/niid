# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-25 19:41
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('niid_db', '0016_auto_20160725_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enclosure',
            name='target_objects',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, null=True, size=None, verbose_name='\u0426\u0435\u043b\u0435\u0432\u044b\u0435 \u043e\u0431\u044a\u0435\u043a\u0442\u044b'),
        ),
    ]
