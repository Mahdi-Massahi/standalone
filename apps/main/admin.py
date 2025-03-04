from django.contrib import admin

# Register your models here.
import apps.main.models as MODELS
from commons.utils import truncate


@admin.register(MODELS.Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "user",
        "title",
        "role",
        "location",
        "category",
        "starting",
        "ending",
    )
    readonly_fields = (
        "model_modified_at",
        "model_created_at",
    )


@admin.register(MODELS.Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "user",
        "type",
        "mode",
        "company",
        "job_title",
        "url",
        "state",
        "contact_name",
        "model_modified_at",
        "ending",
    )
    readonly_fields = (
        "model_modified_at",
        "model_created_at",
    )


@admin.register(MODELS.Tailor)
class TailorAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "application",
        "type",
    )
    readonly_fields = (
        "model_modified_at",
        "model_created_at",
    )
