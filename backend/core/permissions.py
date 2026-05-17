from rest_framework.permissions import BasePermission

from .models import WorkspaceMembership


class IsWorkspaceMember(BasePermission):

    def has_permission(self, request, view):

        workspace_slug = view.kwargs.get(
            'workspace_slug'
        )

        if not workspace_slug:
            return False

        return WorkspaceMembership.objects.filter(
            user=request.user,
            workspace__slug=workspace_slug
        ).exists()