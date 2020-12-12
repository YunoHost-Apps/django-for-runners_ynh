"""
    WSGI config
"""
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'ynh_for_runners_settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()