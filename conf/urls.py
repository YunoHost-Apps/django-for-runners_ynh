from django.conf import settings
from django.conf.urls import static
from django.contrib import admin
from django.urls import path

from for_runners.views.media_files import UserMediaView


if settings.PATH_URL:
    # settings.PATH_URL is the $YNH_APP_ARG_PATH
    # Prefix all urls with "PATH_URL":
    urlpatterns = [
        path(f'{settings.PATH_URL}/', admin.site.urls),
        path(f'{settings.PATH_URL}/media/<slug:user_name>/<path:path>', UserMediaView.as_view()),

        # TODO: https://github.com/jedie/django-for-runners/issues/25
        # path(settings.MEDIA_URL.lstrip('/'), include('django_tools.serve_media_app.urls')),
    ]
    if settings.SERVE_FILES:
        urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
    # Installed to domain root, without a path prefix
    # Just use the default project urls.py
    from for_runners_project.urls import urlpatterns  # noqa
