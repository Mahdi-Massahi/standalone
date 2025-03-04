import os
from datetime import datetime

from core.settings import MEDIA_ROOT
from apps.commons.models import BaseModel, models
from apps.authentication.models import User


class Experience(BaseModel):
    class Type(models.TextChoices):
        FULL_TIME = "FLT", "Full-time"
        PART_TIME = "PRT", "Part-time"
        SELF_EMPLOYED = "SFE", "Self-employed"
        CONTRACT = "CNT", "Contract"

    class Category(models.TextChoices):
        EDUCATION = "EDU", "Education"
        CARRIER = "CRR", "Carrier"
        PROJECT = "PRJ", "Project"

    user = models.ForeignKey(User, models.CASCADE)
    title = models.CharField(max_length=128)
    role = models.CharField(max_length=128)
    location = models.CharField(max_length=128, blank=True, null=True)
    type = models.CharField(max_length=3, choices=Type.choices)
    category = models.CharField(max_length=3, choices=Category.choices)
    url = models.CharField(max_length=1024, blank=True, null=True)
    starting = models.DateTimeField()
    ending = models.DateTimeField(null=True, blank=True)
    description = models.TextField()


class Application(BaseModel):
    class State(models.TextChoices):
        YET_TO_APPLY = "YAP", "Yet to Apply"
        APPLIED = "APL", "Applied"
        REJECTED = "RJC", "Rejected"
        INTERVIEW = "INT", "Interview"
        ACCEPTED = "ACP", "Accepted"

    class Type(models.TextChoices):
        EDUCATION = "PER", "Permanent"
        CARRIER = "CON", "Contract"

    class Mode(models.TextChoices):
        ON_SITE = "OST", "On-Site"
        HYBRID = "HYB", "Hybrid"
        REMOTE = "REM", "Remote"

    user = models.ForeignKey(User, models.CASCADE)
    job_title = models.CharField(max_length=128)
    job_description = models.TextField()
    company = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    type = models.CharField(max_length=3, choices=Type.choices)
    mode = models.CharField(max_length=3, choices=Mode.choices)
    state = models.CharField(max_length=3, choices=State.choices, default=State.APPLIED)
    url = models.URLField(blank=True, null=True)
    contact_name = models.CharField(max_length=128, blank=True, null=True)
    contact_number = models.CharField(max_length=128, blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)


class Tailor(BaseModel):
    class Type(models.TextChoices):
        CV = "CV", "CV"
        ML = "ML", "ML"

    def get_unique_filename(instance: "Tailor", filename):
        folder_name = "tailor"
        time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        unique_filename = f"{instance.application.user.get_full_name()} {time.year}"
        upload_path = os.path.join(MEDIA_ROOT, folder_name, unique_filename)
        return upload_path

    application = models.ForeignKey(Application, models.CASCADE)
    type = models.CharField(max_length=2, choices=Type.choices)
    latex = models.TextField(blank=True, null=True)
    instruction = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to=get_unique_filename, blank=True, null=True)
