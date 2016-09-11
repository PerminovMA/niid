# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-25 10:54
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('niid_db', '0007_auto_20160725_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toxchar',
            name='skin_irritation_1',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), blank=True, choices=[(b'HG_RAB', '\u0412\u044b\u0440\u0430\u0436\u0435\u043d\u043d\u043e\u0435, \u043a\u0440\u043e\u043b\u0438\u043a\u0438'), (b'NO_RAB', '\u0423\u043c\u0435\u0440\u0435\u043d\u043d\u043e\u0435, \u043a\u0440\u043e\u043b\u0438\u043a\u0438'), (b'WE_RAB', '\u0421\u043b\u0430\u0431\u043e\u0435, \u043a\u0440\u043e\u043b\u0438\u043a\u0438'), (b'AB_RAB', '\u041e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0443\u0435\u0442, \u043a\u0440\u043e\u043b\u0438\u043a\u0438'), (b'NO_RAB', '\u041d\u0435 \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u044f\u043b\u0438, \u043a\u0440\u043e\u043b\u0438\u043a\u0438'), (b'HG_PIG', '\u0412\u044b\u0440\u0430\u0436\u0435\u043d\u043d\u043e\u0435, \u043c\u043e\u0440\u0441\u043a\u0438\u0435 \u0441\u0432\u0438\u043d\u043a\u0438'), (b'NO_PIG', '\u0423\u043c\u0435\u0440\u0435\u043d\u043d\u043e\u0435, \u043c\u043e\u0440\u0441\u043a\u0438\u0435 \u0441\u0432\u0438\u043d\u043a\u0438'), (b'WE_PIG', '\u0421\u043b\u0430\u0431\u043e\u0435, \u043c\u043e\u0440\u0441\u043a\u0438\u0435 \u0441\u0432\u0438\u043d\u043a\u0438'), (b'AB_PIG', '\u041e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0443\u0435\u0442, \u043c\u043e\u0440\u0441\u043a\u0438\u0435 \u0441\u0432\u0438\u043d\u043a\u0438'), (b'NO_PIG', '\u041d\u0435 \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u044f\u043b\u0438, \u043c\u043e\u0440\u0441\u043a\u0438\u0435 \u0441\u0432\u0438\u043d\u043a\u0438')], null=True, size=None, verbose_name='\u0420\u0430\u0437\u0434\u0440\u0430\u0436.\u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0435 \u043d\u0430 \u043a\u043e\u0436\u0443'),
        ),
        migrations.AlterField(
            model_name='toxchar',
            name='skin_irritation_2',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), blank=True, choices=[(b'HG_RAB', '\u0412\u044b\u0440\u0430\u0436\u0435\u043d\u043d\u043e\u0435, \u043a\u0440\u043e\u043b\u0438\u043a\u0438'), (b'NO_RAB', '\u0423\u043c\u0435\u0440\u0435\u043d\u043d\u043e\u0435, \u043a\u0440\u043e\u043b\u0438\u043a\u0438'), (b'WE_RAB', '\u0421\u043b\u0430\u0431\u043e\u0435, \u043a\u0440\u043e\u043b\u0438\u043a\u0438'), (b'AB_RAB', '\u041e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0443\u0435\u0442, \u043a\u0440\u043e\u043b\u0438\u043a\u0438'), (b'NO_RAB', '\u041d\u0435 \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u044f\u043b\u0438, \u043a\u0440\u043e\u043b\u0438\u043a\u0438'), (b'HG_PIG', '\u0412\u044b\u0440\u0430\u0436\u0435\u043d\u043d\u043e\u0435, \u043c\u043e\u0440\u0441\u043a\u0438\u0435 \u0441\u0432\u0438\u043d\u043a\u0438'), (b'NO_PIG', '\u0423\u043c\u0435\u0440\u0435\u043d\u043d\u043e\u0435, \u043c\u043e\u0440\u0441\u043a\u0438\u0435 \u0441\u0432\u0438\u043d\u043a\u0438'), (b'WE_PIG', '\u0421\u043b\u0430\u0431\u043e\u0435, \u043c\u043e\u0440\u0441\u043a\u0438\u0435 \u0441\u0432\u0438\u043d\u043a\u0438'), (b'AB_PIG', '\u041e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0443\u0435\u0442, \u043c\u043e\u0440\u0441\u043a\u0438\u0435 \u0441\u0432\u0438\u043d\u043a\u0438'), (b'NO_PIG', '\u041d\u0435 \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u044f\u043b\u0438, \u043c\u043e\u0440\u0441\u043a\u0438\u0435 \u0441\u0432\u0438\u043d\u043a\u0438')], null=True, size=None, verbose_name='\u0420\u0430\u0437\u0434\u0440\u0430\u0436.\u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0435 \u043d\u0430 \u043a\u043e\u0436\u0443 \u043f\u043e\u0432\u0442\u043e\u0440\u043d\u043e\u0435'),
        ),
        migrations.AlterField(
            model_name='toxchar',
            name='tox_skin',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, choices=[(b'DR_1_l100_mouse', 'I \u043a\u043b\u0430\u0441\u0441. \u0427\u0440\u0435\u0437\u0432\u044b\u0447\u0430\u0439\u043d\u043e-\u043e\u043f\u0430\u0441\u043d\u044b\u0435: \u043c\u0435\u043d\u0435\u0435 100, \u043c\u044b\u0448\u0438'), (b'DR_2_100_500_mouse', 'II \u043a\u043b\u0430\u0441\u0441. \u0412\u044b\u0441\u043e\u043a\u043e\u043e\u043f\u0430\u0441\u043d\u044b\u0435: 100-500, \u043c\u044b\u0448\u0438'), (b'DR_3_501_2500_mouse', 'III \u043a\u043b\u0430\u0441\u0441. \u0423\u043c\u0435\u0440\u0435\u043d\u043d\u043e-\u043e\u043f\u0430\u0441\u043d\u044b\u0435: 501-2500, \u043c\u044b\u0448\u0438'), (b'DR_4__m2500_mouse', 'IV \u043a\u043b\u0430\u0441\u0441. \u041c\u0430\u043b\u043e\u043e\u043f\u0430\u0441\u043d\u044b\u0435: \u0431\u043e\u043b\u0435\u0435 2500, \u043c\u044b\u0448\u0438'), (b'DR_1_l100_rats', 'I \u043a\u043b\u0430\u0441\u0441. \u0427\u0440\u0435\u0437\u0432\u044b\u0447\u0430\u0439\u043d\u043e-\u043e\u043f\u0430\u0441\u043d\u044b\u0435: \u043c\u0435\u043d\u0435\u0435 100, \u043a\u0440\u044b\u0441\u044b'), (b'DR_2_100_500_rats', 'II \u043a\u043b\u0430\u0441\u0441. \u0412\u044b\u0441\u043e\u043a\u043e\u043e\u043f\u0430\u0441\u043d\u044b\u0435: 100-500, \u043a\u0440\u044b\u0441\u044b'), (b'DR_3_501_2500_rats', 'III \u043a\u043b\u0430\u0441\u0441. \u0423\u043c\u0435\u0440\u0435\u043d\u043d\u043e-\u043e\u043f\u0430\u0441\u043d\u044b\u0435: 501-2500, \u043a\u0440\u044b\u0441\u044b'), (b'DR_4__m2500_rats', 'IV \u043a\u043b\u0430\u0441\u0441. \u041c\u0430\u043b\u043e\u043e\u043f\u0430\u0441\u043d\u044b\u0435: \u0431\u043e\u043b\u0435\u0435 2500, \u043a\u0440\u044b\u0441\u044b')], null=True, size=None, verbose_name='\u041e\u0441\u0442\u0440\u0430\u044f \u0442\u043e\u043a\u0441\u0438\u0447\u043d\u043e\u0441\u0442\u044c \u043f\u0440\u0438 \u043d\u0430\u043d\u0435\u0441\u0435\u043d\u0438\u0438 \u043d\u0430 \u043a\u043e\u0436\u0443'),
        ),
        migrations.AlterField(
            model_name='toxchar',
            name='tox_stomach',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=30), blank=True, choices=[(b'DR_1_l15_mouse', 'I \u043a\u043b\u0430\u0441\u0441. \u0427\u0440\u0435\u0437\u0432\u044b\u0447\u0430\u0439\u043d\u043e-\u043e\u043f\u0430\u0441\u043d\u044b\u0435: \u043c\u0435\u043d\u0435\u0435 15, \u043c\u044b\u0448\u0438'), (b'DR_2_15_150_mouse', 'II \u043a\u043b\u0430\u0441\u0441. \u0412\u044b\u0441\u043e\u043a\u043e\u043e\u043f\u0430\u0441\u043d\u044b\u0435: 15-150, \u043c\u044b\u0448\u0438'), (b'DR_3_151_5000_mouse', 'III \u043a\u043b\u0430\u0441\u0441. \u0423\u043c\u0435\u0440\u0435\u043d\u043d\u043e-\u043e\u043f\u0430\u0441\u043d\u044b\u0435: 151-5000, \u043c\u044b\u0448\u0438'), (b'DR_4__m5000_mouse', 'IV \u043a\u043b\u0430\u0441\u0441. \u041c\u0430\u043b\u043e\u043e\u043f\u0430\u0441\u043d\u044b\u0435: \u0431\u043e\u043b\u0435\u0435 5000, \u043c\u044b\u0448\u0438'), (b'DR_1_l15_rats', 'I \u043a\u043b\u0430\u0441\u0441. \u0427\u0440\u0435\u0437\u0432\u044b\u0447\u0430\u0439\u043d\u043e-\u043e\u043f\u0430\u0441\u043d\u044b\u0435: \u043c\u0435\u043d\u0435\u0435 15, \u043a\u0440\u044b\u0441\u044b'), (b'DR_2_15_150_rats', 'II \u043a\u043b\u0430\u0441\u0441. \u0412\u044b\u0441\u043e\u043a\u043e\u043e\u043f\u0430\u0441\u043d\u044b\u0435: 15-150, \u043a\u0440\u044b\u0441\u044b'), (b'DR_3_151_5000_rats', 'III \u043a\u043b\u0430\u0441\u0441. \u0423\u043c\u0435\u0440\u0435\u043d\u043d\u043e-\u043e\u043f\u0430\u0441\u043d\u044b\u0435: 151-5000, \u043a\u0440\u044b\u0441\u044b'), (b'DR_4__m5000_rats', 'IV \u043a\u043b\u0430\u0441\u0441. \u041c\u0430\u043b\u043e\u043e\u043f\u0430\u0441\u043d\u044b\u0435: \u0431\u043e\u043b\u0435\u0435 5000, \u043a\u0440\u044b\u0441\u044b')], null=True, size=None, verbose_name='\u041e\u0441\u0442\u0440\u0430\u044f \u0442\u043e\u043a\u0441\u0438\u0447\u043d\u043e\u0441\u0442\u044c \u043f\u0440\u0438 \u0432\u0432\u0435\u0434\u0435\u043d\u0438\u0438 \u0432 \u0436\u0435\u043b\u0443\u0434\u043e\u043a'),
        ),
    ]
