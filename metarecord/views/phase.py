from rest_framework import serializers, viewsets

from metarecord.models import Phase

from .action import ActionDetailSerializer
from .base import DetailSerializerMixin, StructuralElementSerializer


class PhaseListSerializer(StructuralElementSerializer):
    class Meta(StructuralElementSerializer.Meta):
        model = Phase

    actions = serializers.PrimaryKeyRelatedField(many=True, read_only=True)


class PhaseDetailSerializer(PhaseListSerializer):
    actions = ActionDetailSerializer(many=True)


class PhaseViewSet(DetailSerializerMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Phase.objects.all()
    serializer_class = PhaseListSerializer
    serializer_class_detail = PhaseDetailSerializer