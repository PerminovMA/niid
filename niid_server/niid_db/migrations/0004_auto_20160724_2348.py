# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-24 20:48
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('niid_db', '0003_auto_20160724_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toxchar',
            name='board',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255), size=None), size=None),
        ),
    ]
