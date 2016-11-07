from django.db import models
from django.utils.translation import ugettext_lazy as _

from .structural_element import StructuralElement


class Function(StructuralElement):
    function_id = models.CharField(verbose_name=_('function ID'), max_length=16, unique=True, db_index=True, null=True)
    parent = models.ForeignKey('self', verbose_name=_('parent'), related_name='children', blank=True, null=True)
    name = models.CharField(verbose_name=_('name'), max_length=256)
    error_count = models.PositiveIntegerField(default=0)
    is_template = models.BooleanField(verbose_name=_('is template'), default=False)

    # Function attribute validation rules, hardcoded at least for now
    _attribute_validations = {
        'allowed': ['PersonalData', 'PublicityClass', 'SecurityPeriod', 'Restriction.SecurityPeriodStart',
                    'SecurityReason', 'RetentionPeriod', 'RetentionReason', 'RetentionPeriodStart',
                    'AdditionalInformation'],
        'required': ['PersonalData', 'PublicityClass', 'SecurityPeriod', 'Restriction.SecurityPeriodStart',
                     'SecurityReason', 'RetentionPeriod', 'RetentionReason', 'RetentionPeriodStart'],
        'conditionally_required': {
            'SecurityPeriod': {'PublicityClass': 'Salassa pidettävä'},
            'Restriction.SecurityPeriodStart': {'PublicityClass': 'Salassa pidettävä'},
            'SecurityReason': {'PublicityClass': 'Salassa pidettävä'}
        }
    }

    class Meta:
        verbose_name = _('function')
        verbose_name_plural = _('functions')

    def __str__(self):
        if self.is_template:
           return '* %s * %s' % (_('template').upper(), self.name)

        return '%s %s' % (self.function_id, self.name)

    def save(self, *args, **kwargs):
        # templates have function_id None
        if self.is_template:
            self.function_id = None
        # others must have a function_id
        elif not self.function_id:
            raise Exception('function_id cannot be empty or null.')
        super().save(*args, **kwargs)
