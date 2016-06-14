"""
WSGI config for montasola project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys
import site
import django

sys.path.append('/var/www/montasola.com/public_html/montasola')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
django.setup()

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

#from django.core.wsgi import get_wsgi_application
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "montasola.settings")
#application = get_wsgi_application()
