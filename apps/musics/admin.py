from django.contrib import admin

from musics.models import Author


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


admin.site.register(Author, AuthorAdmin)
