# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-25 20:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('niid_db', '0018_enclosure_purpose'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enclosure',
            old_name='purpose',
            new_name='destination',
        ),
    ]