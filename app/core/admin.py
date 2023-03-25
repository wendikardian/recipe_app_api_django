"""Django admin costumization"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# To integrates with Django translation system
from django.utils.translation import gettext_lazy as _

from core import models


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users"""
    ordering = ['id']
    list_display = ['email', 'name']
    # None is the title
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser'
                )
            }
        ),
        (
            _('Important dates'), {
                'fields': ('last_login',)
            }
        )
    )
    readonly_fields=['last_login']


admin.site.register(models.User, UserAdmin)
