from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from musics import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# DEBUG TOOLBAR

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]