from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView


# settings.PATH_URL is the $YNH_APP_ARG_PATH
if settings.PATH_URL:
    admin.autodiscover()

    urlpatterns = [
        # TODO:
        # XXX: Hack - the MEDIA_URL contains the "PATH_URL" already:
        # path(settings.MEDIA_URL.lstrip('/'), include('django_tools.serve_media_app.urls')),

        path(f'{settings.PATH_URL}/admin/', admin.site.urls),
        path('', RedirectView.as_view(pattern_name='admin:index')),
    ]
else:
    # Installed to domain root, without a path prefix?
    from inventory_project.urls import urlpatterns  # noqa
