"""
WSGI config for skincare project.
"""

import os
import sys
from pathlib import Path

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent

# Add the project directory to Python path
sys.path.append(str(BASE_DIR))

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skincare.settings')

# Get WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
