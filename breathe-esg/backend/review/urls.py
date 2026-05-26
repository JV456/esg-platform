from django.urls import path

from .views import (
    DashboardMetricsView,
    PendingReviewListView,
    FlaggedRecordsView,
    ApproveRecordView,
    RejectRecordView,
)

urlpatterns = [

    path(
        "dashboard/",
        DashboardMetricsView.as_view()
    ),

    path(
        "pending/",
        PendingReviewListView.as_view()
    ),

    path(
        "flagged/",
        FlaggedRecordsView.as_view()
    ),

    path(
        "approve/<int:record_id>/",
        ApproveRecordView.as_view()
    ),

    path(
        "reject/<int:record_id>/",
        RejectRecordView.as_view()
    ),
]