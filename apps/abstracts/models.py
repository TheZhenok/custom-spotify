from django.db import models
from django.utils import timezone


class AbstractQuerySet(models.QuerySet):
    """Pre-setup QuerySet for AbstractManager."""

    def delete(self, *args, **kwargs):
        self.update(
            datetime_deleted=timezone.now()
        )


class AbstractManager(models.Manager):
    """Manager for AbstractModel class."""

    


class AbstractModel(models.Model):
    """Abstract model.
    
    For desription all custom models."""

    datetime_created = models.DateTimeField(
        verbose_name="время создание",
        auto_now_add=True
    )
    datetime_updated = models.DateTimeField(
        verbose_name="время обновления",
        auto_now=True
    )
    datetime_deleted = models.DateTimeField(
        verbose_name="время удаления",
        null=True,
        blank=True
    )
    objects = AbstractManager()

    class Meta:
        abstract = True
