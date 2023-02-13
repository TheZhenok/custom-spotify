from django.db import models
from django.db.models import QuerySet

from abstracts.models import (
    AbstractModel,
    AbstractManager,
    AbstractQuerySet
)
from auths.models import CustomUser


class Author(AbstractModel):
    """User but will push music by 5 dollars."""

    datestart_subscribe = models.DateField(
        verbose_name="начало подписки",
        auto_now_add=True
    )
    followers = models.ManyToManyField(
        to=CustomUser,
        related_name="followers",
        verbose_name="подписчики"
    )
    user = models.ForeignKey(
        to=CustomUser,
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
        return self.user.email


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


class MusicManager(AbstractManager):
    """Manager special for Music."""

    def get_music_by_genre(self, title: str) -> QuerySet["Music"]:
        id: str =\
            Genre.objects.get(title=title).id
        return self.filter(
            genre=id
        )



class Music(AbstractModel):
    """Main class for music app."""

    STATUS_PATTERN = [
        ("BR", "Предрелиз"), 
        ("R", "Релиз"),
        ("AR", "Unkown")
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
        default="Unkown"
    )
    image = models.ImageField(
        verbose_name="изображение",
        upload_to="images/",
        default=""
    )
    audio = models.FileField(
        verbose_name="музыка",
        upload_to="musics/"
    )

    class Meta:
        ordering = (
            "-datetime_created",
        )
        verbose_name = "трек"
        verbose_name_plural = "треки"

    def __str__(self) -> str:
        return self.title
