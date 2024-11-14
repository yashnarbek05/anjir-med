from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import (
    User, 
    Doctor, 
    DoctorSpecialize, 
    Patient,
)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['phone_number', 'first_name', 'last_name']
    ordering = []
    fieldsets = (
        (None, {"fields": ("phone_number", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("phone_number", "usable_password", "password1", "password2"),
            },
        ),
    )
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("phone_number", "first_name", "last_name")
    filter_horizontal = (
        "groups",
        "user_permissions",
    )


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    pass


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    pass


@admin.register(DoctorSpecialize)
class DoctorSpecializeAdmin(admin.ModelAdmin):
    pass
