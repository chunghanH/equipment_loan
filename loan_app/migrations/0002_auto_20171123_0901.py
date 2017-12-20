# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-23 01:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loan_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='equip_name',
        ),
        migrations.AlterField(
            model_name='equipment',
            name='equip_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan_app.Group'),
        ),
    ]
