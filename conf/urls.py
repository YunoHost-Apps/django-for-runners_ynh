from django.conf import settings
from django.conf.urls import static
from django.contrib import admin
from django.urls import path


# from django_yunohost_integration.views import request_media_debug_view


if settings.PATH_URL:
    # settings.PATH_URL is the $YNH_APP_ARG_PATH
    # Prefix all urls with "PATH_URL":
    urlpatterns = [
        path(f'{settings.PATH_URL}/', admin.site.urls),
        # path(f'{settings.PATH_URL}/debug/', request_media_debug_view),

        # TODO: https://github.com/jedie/django-for-runners/issues/25
        # MEDIA_URL contains the "PATH_URL" already:
        # path(settings.MEDIA_URL.lstrip('/'), include('django_tools.serve_media_app.urls')),
    ]
    if settings.SERVE_FILES:
        urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
    # Installed to domain root, without a path prefix
    # Just use the default project urls.py
    from for_runners_project.urls import urlpatterns  # noqa
