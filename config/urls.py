from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/auth/", include("apps.users.api.urls")),
    path("api/v1/jobs/", include("apps.jobs.api.urls")),
]
