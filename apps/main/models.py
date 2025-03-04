from apps.commons.models import BaseModel, models
from apps.authentication.models import User


class Experience(BaseModel):
    class Type(models.TextChoices):
        FULL_TIME = "FLT", "Full-time"
        PART_TIME = "PRT", "Part-time"
        SELF_EMPLOYED = "SFE", "Self-employed"
        CONTRACT = "CNT", "Contract"
        EXTRACURRICULAR = "EXT", "Extracurricular"

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
    starting = models.DateField()
    ending = models.DateField(null=True, blank=True)
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

    application = models.ForeignKey(Application, models.CASCADE)
    type = models.CharField(max_length=2, choices=Type.choices)
    latex = models.TextField(blank=True, null=True)
    instruction = models.TextField(blank=True, null=True)
    file = models.FileField(blank=True, null=True)
    fitness = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    meta = models.JSONField(default=dict, blank=True, null=True)
