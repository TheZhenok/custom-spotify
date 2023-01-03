from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from musics.models import (
    Music,
    Genre,
    Author
)


def main(request, *args, **kwargs):
    return render(
        request=request,
        template_name='musics/home_page.html',
        context={}
    )
