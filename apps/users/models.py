from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from apps.users.managers import UserManager
from apps.core.models import BaseModel

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    class Roles(models.TextChoices):
        IS_COMPANY = "is_company", "Is Company"
        IS_CANDIDATE = "is_candidate", "Is Candidate"
    
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    
    roles = models.CharField(
        choices=Roles,
        default=None,
        blank=True, 
        null=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.email
