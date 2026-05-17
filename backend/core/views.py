from django.db.models import Count
from django.core.cache import cache
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Workspace, Event
from .permissions import IsWorkspaceMember


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