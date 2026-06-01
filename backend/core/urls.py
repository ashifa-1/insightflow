# backend/core/urls.py 
from django.urls import path
from .views import (
    DashboardSummaryView,
    OAuthLoginView,
    CurrentUserView,
    LogoutView,
    WorkspaceListCreateView,
    EventIngestView,
    DashboardTimeseriesView
)
urlpatterns = [
    path(
        'w/<slug:workspace_slug>/dashboard/summary/',
        DashboardSummaryView.as_view()
    ),

    path(
        'auth/me/',
        CurrentUserView.as_view(),
    ),

    path(
        'auth/logout/',
        LogoutView.as_view(),
    ),

    path(
        'workspaces/',
        WorkspaceListCreateView.as_view(),
    ),

    path(
        'w/<slug:workspace_slug>/dashboard/timeseries/',
        DashboardTimeseriesView.as_view(),
    ),

    path(
        'auth/<str:provider>/',
        OAuthLoginView.as_view(),
    ),

    path(
        'w/<slug:workspace_slug>/events/',
        EventIngestView.as_view(),
    ),
]
