from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter
from rest_framework import viewsets, permissions

from apps.users.models import User
from apps.users.permissions import IsCompany, IsCandidate
from apps.jobs.models import Job, JobApplication, JobBookmark
from apps.jobs.tasks import send_application_email
from .serializers import JobSerializer, JobApplicationSerializer, JobBookmarkSerializer

def perform_create(self, serializer):
    application = serializer.save(candidate=self.request.user)
    company_email = application.job.company.email
    candidate_name = self.request.user.username
    job_title = application.job.title

    send_application_email.delay(company_email, candidate_name, job_title)

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['location', 'salary', 'job_type']
    search_fields = ['title', 'description']

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), IsCompany()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        serializer.save(company=self.request.user)


class JobApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = JobApplicationSerializer
    queryset = JobApplication.objects.all()

    def get_permissions(self):
        if self.action in ['create']:
            return [permissions.IsAuthenticated(), IsCandidate()]
        if self.action in ['update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), IsCandidate()]
        return [permissions.IsAuthenticated()]  # all users can read

    def get_queryset(self):
        user = self.request.user
        if user.roles == User.Roles.IS_COMPANY:
            return JobApplication.objects.filter(job__company=user)
        if user.roles == User.Roles.IS_CANDIDATE:
            return JobApplication.objects.filter(candidate=user)
        return JobApplication.objects.none()

    def perform_create(self, serializer):
        serializer.save(candidate=self.request.user)
        

class JobBookmarkViewSet(viewsets.ModelViewSet):
    serializer_class = JobBookmarkSerializer

    def get_permissions(self):
        if self.action in ['create', 'destroy', 'list']:
            return [permissions.IsAuthenticated(), IsCandidate()]
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        return JobBookmark.objects.filter(candidate=self.request.user)

    def perform_create(self, serializer):
        serializer.save(candidate=self.request.user)