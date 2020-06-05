from django.core import exceptions
from django.db import transaction
from django.db.models import Prefetch
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers, viewsets

from metarecord.models import Classification, Function
from metarecord.views.function import PhaseSerializer

from .base import HexRelatedField


def include_related(request):
    """
    Convert 'include_related' GET parameter value to boolean.
    Accept 'true' and 'True' as valid values.
    """
    query_param_value = request.GET.get('include_related')
    return (query_param_value in ['true', 'True'])


class ClassificationSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source='uuid', format='hex', read_only=True)
    parent = HexRelatedField(read_only=True)
    modified_by = serializers.SerializerMethodField()

    class Meta:
        model = Classification
        fields = (
            'id',
            'created_at',
            'modified_at',
            'modified_by',
            'version',
            'state',
            'valid_from',
            'valid_to',
            'code',
            'title',
            'parent',
            'description',
            'description_internal',
            'related_classification',
            'additional_information',
            'function_allowed',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        request = self.context['request']
        self.include_related = False

        if request.method == 'GET':
            self.include_related = include_related(request)

    def get_fields(self):
        fields = super().get_fields()

        if self.include_related:
            fields['phases'] = serializers.SerializerMethodField(method_name='_get_phases')

        return fields

    def get_modified_by(self, obj):
        user = self.context['request'].user

        if user.has_perm(Classification.CAN_VIEW_MODIFIED_BY):
            return obj.get_modified_by_display()

        return None

    def _get_function(self, obj):
        functions = obj.prefetched_functions
        num_of_functions = len(functions)

        if num_of_functions > 1:
            raise Exception(
                'Classification %s has more than one functions (%s)' %
                (obj.uuid, [function.uuid for function in functions])
            )

        return functions[0] if num_of_functions else None

    def _append_function_fields_to_repr(self, obj, data):
        function = self._get_function(obj)
        if function:
            data['function'] = function.uuid.hex
            data['function_state'] = function.state
            data['function_attributes'] = function.attributes
            data['function_version'] = function.version
            data['function_valid_from'] = function.valid_from
            data['function_valid_to'] = function.valid_to
        else:
            data['function'] = None
            data['function_state'] = None
            data['function_attributes'] = None
            data['function_version'] = None
            data['function_valid_from'] = None
            data['function_valid_to'] = None

        return data

    def _get_phases(self, obj):
        phases = None
        function = self._get_function(obj)

        if function:
            phases = function.phases.all()

        serializer = PhaseSerializer(phases, many=True)

        return serializer.data

    def to_representation(self, obj):
        data = super().to_representation(obj)
        request = self.context['request']

        if request.method == 'GET':
            data = self._append_function_fields_to_repr(obj, data)

            if request and not request.user.is_authenticated:
                data.pop('description_internal', None)
                data.pop('additional_information', None)

        return data

    @transaction.atomic
    def create(self, validated_data):
        user = self.context['request'].user

        if not user.has_perm(Classification.CAN_EDIT):
            raise exceptions.PermissionDenied(_('No permission to create.'))

        validated_data.update({
            'created_by': user,
            'modified_by': user,
        })

        return super().create(validated_data)


    @transaction.atomic
    def update(self, instance, validated_data):
        user = self.context['request'].user

        if not user.has_perm(Classification.CAN_EDIT):
            raise exceptions.PermissionDenied(_('No permission to update.'))

        validated_data.update({
            'modified_by': user,
        })

        return super().update(instance, validated_data)


class ClassificationViewSet(viewsets.ModelViewSet):
    queryset = Classification.objects.order_by('code').select_related('parent').prefetch_related('children')
    serializer_class = ClassificationSerializer
    lookup_field = 'uuid'

    def get_queryset(self):
        user = self.request.user
        queryset = Function.objects.filter_for_user(user).latest_version()

        if include_related(self.request):
            queryset = queryset.prefetch_related(
                'phases',
                'phases__actions',
                'phases__actions__records'
            )

        return super().get_queryset().prefetch_related(
            Prefetch(
                'functions',
                queryset=queryset,
                to_attr='prefetched_functions'
            )
        )
