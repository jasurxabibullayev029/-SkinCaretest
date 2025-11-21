from setuptools import setup, find_packages
import os

# List of dependencies
INSTALL_REQUIRES = [
    'Django==5.2.7',
    'djangorestframework==3.16.1',
    'django-cors-headers==4.9.0',
    'python-dotenv==1.1.1',
    'pillow==12.0.0',
    'requests==2.32.5',
    'gunicorn==22.0.0',
    'sqlparse==0.5.3',
    'tzdata==2025.2',
    'openai==2.6.1'
]

setup(
    name="skincare_ai",
    version="1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    python_requires='>=3.8',
    package_data={
        '': ['*.html', '*.css', '*.js', '*.png', '*.jpg', '*.jpeg', '*.gif', '*.svg', '*.ico', '*.json'],
    },
)
