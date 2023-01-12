# Python
from typing import Any

# Django
from django.conf import settings
from django.core.mail import send_mail
from django.db.models.base import ModelBase
from django.db.models.signals import (
    post_delete,
    post_save
)
from django.dispatch import receiver

# Local
from auths.models import CustomUser


@receiver(
    post_save,
    sender=CustomUser
)
def post_save_player(
    sender: ModelBase,
    instance: CustomUser,
    created: bool,
    **kwargs: Any
) -> None:
    if created:
        send_mail(
            subject='Activation code',
            message=f'Your link: http://localhost:8000/activate/{instance.activation_code}/',
            from_email='zhenok1109@gmail.com',
            recipient_list=[
                instance.email
            ],
            fail_silently=False
        )