# backend/core/serializers.py
from rest_framework import serializers
from .models import (
    Workspace,
    Event,
    WorkspaceMembership
)

class WorkspaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Workspace

        fields = [
            'id',
            'name',
            'slug',
            'created_at'
        ]

class WorkspaceMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkspaceMembership
        fields = [
            "role",
            "joined_at"
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