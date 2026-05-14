"""ASGI config for katalog_sederhana project."""
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'katalog_sederhana.settings')
application = get_asgi_application()
