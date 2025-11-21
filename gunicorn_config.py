import os
import sys
from pathlib import Path

# Set the working directory to the project root
BASE_DIR = Path(__file__).resolve().parent
chdir = str(BASE_DIR)

# Add the project directory to Python path
sys.path.insert(0, str(BASE_DIR))

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skincare.settings')

# Gunicorn configuration
bind = "0.0.0.0:{}".format(os.environ.get('PORT', '10000'))
workers = 3
worker_class = "sync"
timeout = 120

# Logging
loglevel = 'debug'
errorlog = '-'  # Log to stderr
accesslog = '-'  # Log to stdout

# WSGI application
wsgi_app = "skincare.wsgi:application"
