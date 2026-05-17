from rest_framework import serializers

from .models import Workspace, Event


class WorkspaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Workspace

        fields = [
            'id',
            'name',
            'slug',
            'created_at'
        ]


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event

        fields = [
            'id',
            'event_name',
            'payload',
            'created_at'
        ]