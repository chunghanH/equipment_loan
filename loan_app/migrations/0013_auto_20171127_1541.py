# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-27 07:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan_app', '0012_auto_20171127_1539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='location',
        ),
        migrations.RemoveField(
            model_name='group',
            name='unit',
        ),
        migrations.RemoveField(
            model_name='group',
            name='yaer',
        ),
        migrations.AddField(
            model_name='equipment',
            name='location',
            field=models.CharField(default=11, max_length=256, verbose_name='使用地點'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipment',
            name='unit',
            field=models.CharField(default=11, max_length=256, verbose_name='使用單位'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipment',
            name='yaer',
            field=models.CharField(default=1, max_length=256, verbose_name='採購年度'),
            preserve_default=False,
        ),
    ]