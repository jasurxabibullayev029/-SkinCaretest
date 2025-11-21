from setuptools import setup, find_packages
import os

# Read requirements from requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="skincare_ai",
    version="1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    python_requires='>=3.8',
    package_data={
        '': ['*.html', '*.css', '*.js', '*.png', '*.jpg', '*.jpeg', '*.gif', '*.svg', '*.ico', '*.json'],
    },
    entry_points={
        'console_scripts': [
            'skincare_ai=manage:main',
        ],
    },
)
