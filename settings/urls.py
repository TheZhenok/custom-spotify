from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from musics.views import (
    MainView,
    MusicView,
    TempView,
)
from auths.views import (
    RegistrationView,
    LoginView,
    LogoutView,
    ProfileView,
    EditView,
    ChangePassowrdView,
    activate_user
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view()),
    path('music/', MusicView.as_view()),
    path('temp/', TempView.as_view()),
    path('activate/<str:code>/', activate_user),
    path('auths/', LoginView.as_view()),
    path('auths/registration', RegistrationView.as_view()),
    path('auths/log-out', LogoutView.as_view()),
    path('auths/profile', ProfileView.as_view()),
    path('auths/edit', EditView.as_view()),
    path('auths/change-password', ChangePassowrdView.as_view()),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# DEBUG TOOLBAR

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]