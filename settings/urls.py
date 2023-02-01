from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from musics.views import (
    MainView,
    MusicView,
    TempView,
)
from auths import views as au_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view()),
    path('music/', MusicView.as_view()),
    path('temp/', TempView.as_view()),
    path('activate/<str:code>/', au_views.activate_user)
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# DEBUG TOOLBAR

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]