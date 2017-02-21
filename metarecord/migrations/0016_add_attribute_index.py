# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-02-16 14:30
from __future__ import unicode_literals

from django.db import migrations, models


def add_indexes(apps, schema_editor):
    Attribute = apps.get_model('metarecord', 'Attribute')
    for attribute in Attribute.objects.all():
        attribute.index = max(Attribute.objects.values_list('index', flat=True) or [0]) + 1
        attribute.save()


class Migration(migrations.Migration):

    dependencies = [
        ('metarecord', '0015_versionable_functions'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attribute',
            options={'ordering': ('index',), 'verbose_name': 'attribute', 'verbose_name_plural': 'attributes'},
        ),
        migrations.AddField(
            model_name='attribute',
            name='index',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.RunPython(add_indexes, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='attribute',
            name='index',
            field=models.PositiveSmallIntegerField(db_index=True),
        ),
    ]
