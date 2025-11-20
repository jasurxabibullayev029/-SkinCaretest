"""
WSGI entry point for Render deployment.
This file helps Gunicorn locate the Django WSGI application.
"""

import os
import sys
from pathlib import Path

# Add the project directory to the Python path
project_root = str(Path(__file__).resolve().parent)
if project_root not in sys.path:
    sys.path.append(project_root)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skincare_ai.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
