from django.db import models
from django.conf import settings

from apps.core.models import BaseModel
from apps.users.models import User

class Job(BaseModel):
    JOB_TYPES = [
        ('FT', 'Full-Time'),
        ('PT', 'Part-Time'),
        ('RM', 'Remote'),
        ('CT', 'Contract'),
        ('IN', 'Internship'),
    ]
    
    company = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs')
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    job_type = models.CharField(max_length=2, choices=JOB_TYPES)

    def __str__(self):
        return self.title
    
class JobApplication(BaseModel):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    candidate = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='applications')
    cover_letter = models.TextField(blank=True)

    class Meta:
        unique_together = ('job', 'candidate')  # prevent double apply

    def __str__(self):
        return f"{self.candidate.username} → {self.job.title}"

class JobBookmark(BaseModel):
    candidate = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookmarks')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='bookmarked_by')
    bookmarked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('candidate', 'job')  # one bookmark per job per user

    def __str__(self):
        return f"{self.candidate.username} 🔖 {self.job.title}"
