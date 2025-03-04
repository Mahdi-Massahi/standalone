from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    bio = models.TextField()
    phone = models.CharField(max_length=32)
    location = models.CharField(max_length=32)
    company = models.CharField(max_length=32)
    linkedin = models.CharField(max_length=128)
    github = models.CharField(max_length=128)
    website = models.CharField(max_length=128)
    summary = models.CharField(max_length=128)
    languages = models.JSONField(default="")
    soft_skills = models.JSONField(default="")
    hard_skills = models.JSONField(default="")
