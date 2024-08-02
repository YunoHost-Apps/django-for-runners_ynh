from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from for_runners.views.media_files import UserMediaView


if settings.PATH_URL:
    # settings.PATH_URL is __PATH__
    # Prefix all urls with "PATH_URL":
    urlpatterns = [
        path('', RedirectView.as_view(url=f'{settings.PATH_URL}/')),
        path(f'{settings.PATH_URL}/media/<slug:user_name>/<path:path>', UserMediaView.as_view()),
        # TODO: https://github.com/jedie/django-for-runners/issues/25
        # path(settings.MEDIA_URL.lstrip('/'), include('django_tools.serve_media_app.urls')),
        path(f'{settings.PATH_URL}/', admin.site.urls),
    ]
else:
    # Installed to domain root, without a path prefix
    # Just use the default project urls.py
    from for_runners_project.urls import urlpatterns  # noqa
