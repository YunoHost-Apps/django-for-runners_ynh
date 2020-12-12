from django.conf import settings
from django.conf.urls import include, static, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from for_runners.views.media_files import UserMediaView

admin.autodiscover()


urlpatterns = i18n_patterns(
    path("{settings.PATH_URL}/admin/", admin.site.urls),

    # FIXME:
    # until there is not real CMS pages: redirect to the interesting admin page:
    url(r"^{settings.PATH_URL}/$", RedirectView.as_view(pattern_name='admin:index')),
)


urlpatterns = [
    # TODO: Change from user name to ID?
    path('{settings.PATH_URL}/media/<slug:user_name>/<path:path>', UserMediaView.as_view()),
] + urlpatterns

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [url(r'^__debug__/', include(debug_toolbar.urls))] + urlpatterns
