# Generated by Django 2.2.12 on 2020-06-05 09:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('metarecord', '0046_classification_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='classification',
            name='_created_by',
            field=models.CharField(blank=True, editable=False, max_length=200, verbose_name='created by (text)'),
        ),
        migrations.AddField(
            model_name='classification',
            name='_modified_by',
            field=models.CharField(blank=True, editable=False, max_length=200, verbose_name='modified by (text)'),
        ),
        migrations.AddField(
            model_name='classification',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='classification_created', to=settings.AUTH_USER_MODEL, verbose_name='created by'),
        ),
        migrations.AddField(
            model_name='classification',
            name='modified_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='classification_modified', to=settings.AUTH_USER_MODEL, verbose_name='modified by'),
        ),
        migrations.AddField(
            model_name='classification',
            name='state',
            field=models.CharField(choices=[('draft', 'Draft'), ('sent_for_review', 'Sent for review'), ('waiting_for_approval', 'Waiting for approval'), ('approved', 'Approved')], default='draft', max_length=20, verbose_name='state'),
        ),
        migrations.AddField(
            model_name='classification',
            name='valid_from',
            field=models.DateField(blank=True, null=True, verbose_name='valid from'),
        ),
        migrations.AddField(
            model_name='classification',
            name='valid_to',
            field=models.DateField(blank=True, null=True, verbose_name='valid to'),
        ),
        migrations.AddField(
            model_name='classification',
            name='version',
            field=models.PositiveIntegerField(blank=True, db_index=True, default=1, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='classification',
            unique_together={('uuid', 'version')},
        ),
    ]