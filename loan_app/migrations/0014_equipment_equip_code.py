# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-27 08:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan_app', '0013_auto_20171127_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='equip_code',
            field=models.BooleanField(default=True),
        ),
    ]
