from django.db import transaction
from django.dispatch import receiver
from django.db.models.signals import post_save

from apps.main.logics import tailor_cv, tailor_ml
import apps.main.models as MODELS


@transaction.atomic()
@receiver(post_save, sender=MODELS.Application)
def post_save_application(
    sender,
    instance: MODELS.Application,
    created: bool,
    **kwargs,
):
    cv = MODELS.Tailor.objects.filter(
        type=MODELS.Tailor.Type.CV,
        application=instance,
    ).last()
    if cv:
        tailor_cv(cv)

    ml = MODELS.Tailor.objects.filter(
        type=MODELS.Tailor.Type.ML,
        application=instance,
    ).last()
    if ml:
        tailor_ml(ml)
