# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-04-26 10:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metarecord', '0024_attibute_value_index_unique'),
    ]

    operations = [
        migrations.AddField(
            model_name='attribute',
            name='help_text',
            field=models.TextField(blank=True, verbose_name='help text'),
        ),
    ]
