# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-25 21:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('niid_db', '0021_auto_20160725_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passport',
            name='tox_char',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='niid_db.ToxChar', verbose_name='\u0422\u043e\u043a\u0441\u0438\u043a\u043e\u043b\u043e\u0433\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0430'),
        ),
    ]