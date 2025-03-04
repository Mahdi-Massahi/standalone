from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class UserAdmin(BaseUserAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
    )
    fieldsets = BaseUserAdmin.fieldsets + (
        (
            "Custom fields",
            {
                "fields": (
                    "bio",
                    "phone",
                    "location",
                    "company",
                    "linkedin",
                    "github",
                    "website",
                    "summary",
                    "languages",
                    "soft_skills",
                    "hard_skills",
                ),
            },
        ),
    )


admin.site.register(User, UserAdmin)
