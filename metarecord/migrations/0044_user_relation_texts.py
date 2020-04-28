# Generated by Django 2.2.12 on 2020-04-28 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metarecord', '0043_add_name_and_help_text_to_attribute_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='_created_by',
            field=models.CharField(blank=True, editable=False, max_length=200, verbose_name='created by (text)'),
        ),
        migrations.AddField(
            model_name='action',
            name='_modified_by',
            field=models.CharField(blank=True, editable=False, max_length=200, verbose_name='modified by (text)'),
        ),
        migrations.AddField(
            model_name='bulkupdate',
            name='_approved_by',
            field=models.CharField(blank=True, editable=False, max_length=200, verbose_name='approved by (text)'),
        ),
        migrations.AddField(
            model_name='bulkupdate',
            name='_created_by',
            field=models.CharField(blank=True, editable=False, max_length=200, verbose_name='created by (text)'),
        ),
        migrations.AddField(
            model_name='bulkupdate',
            name='_modified_by',
            field=models.CharField(blank=True, editable=False, max_length=200, verbose_name='modified by (text)'),
        ),
        migrations.AddField(
            model_name='function',
            name='_created_by',
            field=models.CharField(blank=True, editable=False, max_length=200, verbose_name='created by (text)'),
        ),
        migrations.AddField(
            model_name='function',
            name='_modified_by',
            field=models.CharField(blank=True, editable=False, max_length=200, verbose_name='modified by (text)'),
        ),
        migrations.AddField(
            model_name='metadataversion',
            name='_modified_by',
            field=models.CharField(blank=True, editable=False, max_length=200, verbose_name='modified by (text)'),
        ),
        migrations.AddField(
            model_name='phase',
            name='_created_by',
            field=models.CharField(blank=True, editable=False, max_length=200, verbose_name='created by (text)'),
        ),
        migrations.AddField(
            model_name='phase',
            name='_modified_by',
            field=models.CharField(blank=True, editable=False, max_length=200, verbose_name='modified by (text)'),
        ),
        migrations.AddField(
            model_name='record',
            name='_created_by',
            field=models.CharField(blank=True, editable=False, max_length=200, verbose_name='created by (text)'),
        ),
        migrations.AddField(
            model_name='record',
            name='_modified_by',
            field=models.CharField(blank=True, editable=False, max_length=200, verbose_name='modified by (text)'),
        ),
    ]