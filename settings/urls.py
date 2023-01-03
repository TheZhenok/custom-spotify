from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
]


# DEBUG TOOLBAR

urlpatterns += [
    path('__debug__/', include('debug_toolbar.urls')),
]
