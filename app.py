"""
WSGI config for skincare_ai project.
"""

import os
import sys
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent

# Add the project directory to the Python path
sys.path.insert(0, str(BASE_DIR))
# Add the skincare_ai package to the path
sys.path.insert(0, os.path.join(BASE_DIR, 'skincare_ai'))

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SkinCareProject.settings')

# This application object is used by any WSGI server configured to use this file.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
