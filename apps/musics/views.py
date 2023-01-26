# Python
from typing import Any

# Django
from django.shortcuts import render
from django.db.models import QuerySet
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.http import (
    HttpRequest,
    HttpResponse,
    QueryDict,
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
from abstracts.mixins import HttpResponseMixin


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


class MusicView(HttpResponseMixin, View):
    """View special for Music model."""

    def get(
        self, 
        request: HttpRequest, 
        *args: tuple, 
        **kwargs: dict
    ) -> HttpResponse:
        status: list[tuple[str]] = Music.STATUS_PATTERN
        genres: QuerySet[Genre] = Genre.objects.all()
        return self.get_http_response(
            request=request,
            template_name='musics/music_create_page.html',
            context={
                'ctx_status': status,
                'ctx_genre': genres
            }
        )

    def post(
        self, 
        request: HttpRequest, 
        *args: tuple, 
        **kwargs: dict
    ) -> HttpResponse:

        data: QueryDict = request.POST
        title = data.get('title')
        duration = data.get('duration')
        author = Author.objects.first()
        genres_id: list = data.getlist('genre')
        music: Music = Music.objects.create(
            title=title,
            duration=duration,
            author=author
        )
        genres: QuerySet[Genre] =\
            Genre.objects.filter(id__in=genres_id)
        
        music.genre.set(genres)

        return HttpResponse("Ok")
