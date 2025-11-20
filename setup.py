from setuptools import setup, find_packages

setup(
    name="skincare_project",
    version="1.0",
    packages=find_packages(),
    install_requires=[
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
)
