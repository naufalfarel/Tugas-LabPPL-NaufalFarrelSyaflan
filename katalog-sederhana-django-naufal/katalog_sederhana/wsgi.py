"""WSGI config for katalog_sederhana project."""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'katalog_sederhana.settings')
application = get_wsgi_application()
