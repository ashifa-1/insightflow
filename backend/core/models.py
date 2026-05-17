from django.db import models
from django.conf import settings
from django.core.cache import cache

class Workspace(models.Model):
    name = models.CharField(max_length=200)

    slug = models.SlugField(
        unique=True
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='owned_workspaces',
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


class WorkspaceMembership(models.Model):

    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('member', 'Member'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    workspace = models.ForeignKey(
        Workspace,
        related_name='memberships',
        on_delete=models.CASCADE
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='member'
    )

    joined_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        unique_together = ('user', 'workspace')

    def __str__(self):
        return f"{self.user} -> {self.workspace}"


class Event(models.Model):

    EVENT_TYPES = [
        ('page_view', 'Page View'),
        ('click', 'Click'),
        ('signup', 'Signup'),
    ]

    workspace = models.ForeignKey(
        Workspace,
        related_name='events',
        on_delete=models.CASCADE
    )
    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)

        cache_key = (
            f"workspaces:{self.workspace.id}:dashboard_summary"
        )

        cache.delete(cache_key)
    
    event_name = models.CharField(
        max_length=50,
        choices=EVENT_TYPES
    )

    payload = models.JSONField(
        default=dict
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        indexes = [
            models.Index(
                fields=['workspace', 'created_at']
            ),

            models.Index(
                fields=['workspace', 'event_name']
            )
        ]

    def __str__(self):
        return f"{self.event_name} - {self.workspace.name}"