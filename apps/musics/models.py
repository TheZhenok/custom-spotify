from django.db import models
from django.contrib.auth.models import User

from abstracts.models import AbstractModel


class Author(AbstractModel):
    """User but will push music by 5 dollars."""

    datestart_subscribe = models.DateField(
        verbose_name="начало подписки",
        auto_now_add=True
    )
    followers = models.ManyToManyField(
        to=User,
        related_name="followers",
        verbose_name="подписчики"
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name="пользователь"
    )

    class Meta:
        ordering = (
            "-datetime_created",
        )
        verbose_name = "автор"
        verbose_name_plural = "авторы"

    def __str__(self) -> str:
        return self.user.username


class Genre(AbstractModel):
    """Have all music genres."""

    title = models.CharField(
        verbose_name="жанр",
        max_length=40,
        unique=True
    )

    class Meta:
        ordering = (
            "title",
        )
        verbose_name = "жанр"
        verbose_name_plural = "жанры"

    def __str__(self) -> str:
        return self.title


class Music(AbstractModel):
    """Main class for music app."""

    STATUS_PATTERN = [
        ('BR', 'Предрелиз'), 
        ('R', 'Релиз'),
        ('AR', 'Unkown')
    ]

    title = models.CharField(
        verbose_name="заголовок",
        max_length=200
    )
    duration = models.TimeField(
        verbose_name="продолжительность"
    )
    author = models.ForeignKey(
        to="Author",
        on_delete=models.CASCADE,
        verbose_name="автор"
    )
    genre = models.ManyToManyField(
        to="Genre",
        verbose_name="жанр"
    )
    status = models.CharField(
        max_length=100,
        verbose_name="статус",
        choices=STATUS_PATTERN,
        default='Unkown'
    )

    class Meta:
        ordering = (
            "-datetime_created",
        )
        verbose_name = "трек"
        verbose_name_plural = "треки"

    def __str__(self) -> str:
        return self.title
