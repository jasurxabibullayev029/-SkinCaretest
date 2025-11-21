"""
WSGI config for skincare_ai project.
"""

import os
import sys
from pathlib import Path

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent

# Add the project directory to Python path
sys.path.insert(0, str(BASE_DIR))

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SkinCareProject.settings')

# Initialize Django
import django
django.setup()

# Get WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
