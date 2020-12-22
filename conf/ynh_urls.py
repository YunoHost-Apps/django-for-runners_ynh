from django.conf import settings
from django.contrib import admin
from django.urls import path

# def debug_view(request):
#     """ debug request.META """
#     if not request.user.is_authenticated:
#         from django.shortcuts import redirect
#         return redirect('admin:index')
#
#     import pprint
#     meta = pprint.pformat(request.META)
#     html = f'<html><body>request.META: <pre>{meta}</pre></body></html>'
#     from django.http import HttpResponse
#     return HttpResponse(html)


admin.autodiscover()

urlpatterns = [
    # path(f'{settings.PATH_URL}/debug/', debug_view),
    path(f'{settings.PATH_URL}/', admin.site.urls),
]
