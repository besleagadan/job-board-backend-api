from django.urls import path

from .views import JobViewSet, JobApplicationViewSet, JobBookmarkViewSet

app_name = "job"

urlpatterns = [
    path("", JobViewSet.as_view({'get': 'list'}), name="job_list"),
    path("applications/", JobApplicationViewSet.as_view({'get': 'list'}), name="application"),
    path("bookmarks/", JobBookmarkViewSet.as_view({'get': 'list'}), name="bookmark"),
]
