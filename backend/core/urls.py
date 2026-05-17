from django.urls import path

from .views import DashboardSummaryView


urlpatterns = [

    path(
        'w/<slug:workspace_slug>/dashboard/summary/',
        DashboardSummaryView.as_view()
    ),
]