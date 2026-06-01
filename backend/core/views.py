from django.db.models import Count
from django.core.cache import cache
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)
from .permissions import IsWorkspaceMember
from django.utils.text import slugify

from .models import (
    Workspace,
    Event,
    WorkspaceMembership
)

from .serializers import (
    WorkspaceSerializer,
    EventCreateSerializer
)

class DashboardSummaryView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsWorkspaceMember
    ]

    def get(self, request, workspace_slug):

        workspace = get_object_or_404(
            Workspace,
            slug=workspace_slug
        )

        cache_key = (
            f"workspaces:{workspace.id}:dashboard_summary"
        )

        cached_data = cache.get(cache_key)

        if cached_data:
            return Response(cached_data)

        event_count = Event.objects.filter(
            workspace=workspace
        ).count()

        top_pages = (
            Event.objects
            .filter(
                workspace=workspace,
                event_name='page_view'
            )
            .values('payload__page')
            .annotate(
                view_count=Count('id')
            )
            .order_by('-view_count')[:10]
        )

        data = {
            'workspace': workspace.name,
            'event_count': event_count,
            'top_pages': list(top_pages)
        }

        cache.set(
            cache_key,
            data,
            timeout=60 * 15
        )

        return Response(data)

class WorkspaceListCreateView(
    APIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        workspaces = Workspace.objects.filter(
            memberships__user=request.user
        ).distinct()

        serializer = WorkspaceSerializer(
            workspaces,
            many=True
        )

        return Response(
            serializer.data
        )

    def post(self, request):

        name = request.data.get("name")

        if not name:
            return Response(
                {
                    "error":
                    "Workspace name required"
                },
                status=400
            )

        slug = slugify(name)
        if Workspace.objects.filter(slug=slug).exists():
            return Response(
                {"error": "Workspace already exists"},
                status=400
            )

        workspace = Workspace.objects.create(
            name=name,
            slug=slug,
            owner=request.user
        )

        WorkspaceMembership.objects.create(
            user=request.user,
            workspace=workspace,
            role="admin"
        )

        serializer = WorkspaceSerializer(
            workspace
        )

        return Response(
            serializer.data,
            status=201
        )

class OAuthLoginView(APIView):

    permission_classes = [AllowAny]

    def get(self, request, provider):

        return Response({
            'message': f'{provider} OAuth initiated'
        })


class CurrentUserView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        return Response({
            "id": request.user.id,
            "username": request.user.username,
            "email": request.user.email,
        })

class EventIngestView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsWorkspaceMember
    ]

    def post(
        self,
        request,
        workspace_slug
    ):

        serializer = (
            EventCreateSerializer(
                data=request.data
            )
        )

        serializer.is_valid(
            raise_exception=True
        )

        workspace = get_object_or_404(
            Workspace,
            slug=workspace_slug
        )

        event = Event.objects.create(
            workspace=workspace,
            event_name=serializer.validated_data[
                "event"
            ],
            payload=serializer.validated_data[
                "payload"
            ]
        )

        return Response(
            {
                "id": event.id,
                "message":
                "Event created"
            },
            status=201
        )

class LogoutView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def post(self, request):

        logout(request)

        return Response({
            "message": "Logged out successfully"
        })