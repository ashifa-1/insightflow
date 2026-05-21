from django.urls import path

from .views import DashboardSummaryView
from .views import OAuthLoginView

urlpatterns = [

    path(
        'w/<slug:workspace_slug>/dashboard/summary/',
        DashboardSummaryView.as_view()
    ),
    path(
        'auth/<str:provider>/',
        OAuthLoginView.as_view(),
    ),
]