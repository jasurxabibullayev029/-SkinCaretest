"""
WSGI entry point for Render deployment.
This file helps Gunicorn locate the Django WSGI application.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skincare_ai.settings')

application = get_wsgi_application()
