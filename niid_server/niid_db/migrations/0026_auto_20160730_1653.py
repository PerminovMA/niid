# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-30 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('niid_db', '0025_auto_20160729_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='toxchar',
            name='obyv_atmosphere',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=7, max_length=100, null=True, verbose_name='\u041e\u0411\u0423\u0412 \u0432 \u0430\u0442\u043c\u043e\u0441\u0444\u0435\u0440\u043d\u043e\u043c \u0432\u043e\u0437\u0434\u0443\u0445\u0435'),
        ),
        migrations.AddField(
            model_name='toxchar',
            name='obyv_work_zone',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=7, max_length=100, null=True, verbose_name='\u041e\u0411\u0423\u0412 \u0432 \u0432\u043e\u0437\u0434\u0443\u0445\u0435 \u0440\u0430\u0431\u043e\u0447\u0435\u0439 \u0437\u043e\u043d\u044b'),
        ),
        migrations.AlterField(
            model_name='toxchar',
            name='pdk_atmosphere',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=7, max_length=100, null=True, verbose_name='\u041f\u0414\u041a \u0432 \u0430\u0442\u043c\u043e\u0441\u0444\u0435\u0440\u043d\u043e\u043c \u0432\u043e\u0437\u0434\u0443\u0445\u0435'),
        ),
        migrations.AlterField(
            model_name='toxchar',
            name='pdk_work_zone',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=7, max_length=100, null=True, verbose_name='\u041f\u0414\u041a \u0432 \u0432\u043e\u0437\u0434\u0443\u0445\u0435 \u0440\u0430\u0431\u043e\u0447\u0435\u0439 \u0437\u043e\u043d\u044b'),
        ),
    ]
