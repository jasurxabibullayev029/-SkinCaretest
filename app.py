"""
WSGI config for skincare_ai project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os
import skincare_ai
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skincare_ai.settings')

application = get_wsgi_application()
