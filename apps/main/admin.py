from django.contrib import admin

import apps.main.models as MODELS


class TailorInline(admin.StackedInline):
    model = MODELS.Tailor
    extra = 2
    max_num = 2
    show_change_link = True
    fields = [
        "id",
        "type",
        "latex",
        "instruction",
        "file",
    ]
    readonly_fields = (
        "model_modified_at",
        "model_created_at",
    )


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


@admin.register(MODELS.Tailor)
class TailorAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "application",
        "type",
        "file",
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
        "state",
        "contact_name",
        "model_modified_at",
    )
    readonly_fields = (
        "model_modified_at",
        "model_created_at",
    )
    inlines = [TailorInline]
