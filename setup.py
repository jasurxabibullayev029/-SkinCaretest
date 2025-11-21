from setuptools import setup, find_packages
import os

# Read requirements from requirements.txt
with open('requirements.txt') as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name="SkinCareProject",
    version="1.0.0",
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    install_requires=requirements,
    python_requires='>=3.8',
    author="Your Name",
    author_email="your.email@example.com",
    description="Skin Care Project",
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/SkinCareProject",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_data={
        '': ['*.html', '*.css', '*.js', '*.png', '*.jpg', '*.jpeg', '*.gif', '*.svg', '*.ico', '*.json'],
    },
)
