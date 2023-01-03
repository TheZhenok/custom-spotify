from django.db import models
from django.contrib.auth.models import User

from abstracts.models import AbstractModel


class Author(AbstractModel):
    """User but will push music by 5 dollars."""

    datestart_subscribe = models.DateField(
        verbose_name='начало подписки',
        auto_now_add=True
    )
    followers = models.ManyToManyField(
        to=User,
        related_name='followers',
        verbose_name='подписчики'
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='пользователь'
    )

    class Meta:
        ordering = (
            '-datetime_created',
        )
        verbose_name = 'автор'
        verbose_name_plural = 'авторы'

    def __str__(self) -> str:
        return self.user.username
