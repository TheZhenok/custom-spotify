# Django
from django.shortcuts import render
from django.db.models import QuerySet
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.http import (
    HttpRequest,
    HttpResponse,
)
from django.views.generic import (
    View,
    ListView,
)

# Local
from musics.models import (
    Music,
    Genre,
    Author
)


class MainView(View):
    """Main view."""

    queryset: QuerySet = Music.objects.all()

    def get(self, request: HttpRequest, *args, **kwargs):
        u: QuerySet
        try:
            u = Music.objects.filter(
                genre=Genre.objects.get(title='Рок').id
            )
        except:
            u = {}

        return render(
            request=request,
            template_name='musics/home_page.html',
            context={
                'u': u
            }
        )


class MusicView(View):
    """View special for Music model."""

    def get(self, request: HttpRequest, *args, **kwargs):
        status: list[tuple[str]] = Music.STATUS_PATTERN
        genres: QuerySet[Genre] = Genre.objects.all()
        return render(
            request=request,
            template_name='musics/music_create_page.html',
            context={
                'ctx_status': status,
                'ctx_genre': genres
            }
        )

