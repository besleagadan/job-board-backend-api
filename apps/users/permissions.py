from rest_framework.permissions import BasePermission
from .models import User

class IsCompany(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.roles == User.Roles.IS_COMPANY

class IsCandidate(BasePermission):
    def has_permission(self, request, view):
        return request.user and  request.user.roles == User.Roles.IS_CANDIDATE
