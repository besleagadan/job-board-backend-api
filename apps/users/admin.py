from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from apps.users.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'full_name', 'is_staff', 'is_verified')
    list_filter = ('is_staff', 'is_superuser', 'is_verified')
    ordering = ('-date_joined',)
    search_fields = ('email', 'full_name')
    readonly_fields = (
        'created_by', 'created_at', 'updated_by', 'updated_at',
        'deleted_by','deleted_at', 'date_joined'
    )

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('full_name', 'phone')}),
        (
            'Permissions', {
                'fields': (
                    'is_active', 'is_staff', 'is_superuser', 'is_verified', # , 'groups', 'user_permissions',
                    'roles',
                )
            }
        ),
        ('Important dates', {
            'classes': ('collapse',),
            'fields': (
                'date_joined', 'created_by', 'created_at', 'updated_by', 'updated_at',
                'deleted_by','deleted_at', 'is_deleted'
            )}
        ),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'password1', 'password2', 'is_staff', 'is_superuser'),
        }),
    )
