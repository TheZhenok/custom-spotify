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
from django.core.files.uploadedfile import InMemoryUploadedFile

# Local
from musics.models import (
    Music,
    Genre,
    Author
)
from abstracts.mixins import HttpResponseMixin
from abstracts import utils
from musics.forms import (
    TempForm,
    MusicForm,
)


class MainView(HttpResponseMixin, View):
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

        return self.get_http_response(
            request=request,
            template_name='musics/home_page.html',
            context={
                'u': u,
                'ctx_user': request.user
            }
        )


class MusicView(HttpResponseMixin, View):
    """View special for Music model."""

    form = MusicForm

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
            template_name='musics/temp_html.html',
            context={
                'ctx_status': status,
                'ctx_genre': genres,
                'ctx_form': self.form()
            }
        )

    def post(
        self, 
        request: HttpRequest, 
        *args: tuple, 
        **kwargs: dict
    ) -> HttpResponse:

        images: InMemoryUploadedFile =\
            request.FILES.get('image')
        
        images.name = utils.generate_string() + ".png"
        data: MusicForm = self.form(
            request.POST,
            request.FILES
        )
        if not data.is_valid():
            return HttpResponse("BAD")
        
        print(data.cleaned_data)
        data.save()

        return HttpResponse("Ok")

    def delete(
        self, 
        request: HttpRequest, 
        *args: tuple, 
        **kwargs: dict
    ) -> HttpResponse:
        ...

    def put(
        self, 
        request: HttpRequest, 
        *args: tuple, 
        **kwargs: dict
    ) -> HttpResponse:
        ...


class TempView(HttpResponseMixin, View):
    """Temp.
    
    Just delete later."""

    form = TempForm

    def get(
        self, 
        request: HttpRequest, 
        *args: tuple, 
        **kwargs: dict
    ) -> HttpResponse:
        return self.get_http_response(
            request=request,
            template_name='musics/temp_html.html',
            context={
                'ctx_form': self.form()
            }
        )

    def post(
        self, 
        request: HttpRequest, 
        *args: tuple, 
        **kwargs: dict
    ) -> HttpResponse:
        form: TempForm = self.form(
            request.POST or None
        )
        breakpoint()
        return HttpResponse("Ok")
