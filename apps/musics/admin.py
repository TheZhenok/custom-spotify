from django.contrib import admin

from musics.models import (
    Author,
    Genre,
    Music,
)


class AuthorAdmin(admin.ModelAdmin):
    model = Author
    list_display = [
        'datetime_created',
        'datestart_subscribe',
        'user'
    ]
    readonly_fields = (
        'datetime_created',
        'datetime_updated',
        'datestart_subscribe',
        'followers',
    )


class GenreAdmin(admin.ModelAdmin):
    model = Genre


class MusicAdmin(admin.ModelAdmin):
    model = Music
    list_display = [
        'datetime_created',
        'title',
        'author',
        'status'
    ]
    readonly_fields = (
        'datetime_created',
        'datetime_updated',
    )


admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Music, MusicAdmin)
