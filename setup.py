#!/usr/bin/env python
import os
from setuptools import setup, find_packages

def fread(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='djangopypi2',
    version=fread('VERSION').strip(),
    description="A Django application that emulates the Python Package Index.",
    long_description=fread("README.rst"),
    keywords='django pypi packaging index',
    author='Ask Solem',
    author_email='askh@opera.com',
    maintainer='Zohar Zilberman',
    maintainer_email='popen2@gmail.com',
    url='http://github.com/popen2/djangopypi2',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,

    entry_points = {
        'console_scripts': [
            'manage-pypi-site = djangopypi2.manage_pypi_site:main',
        ],
    },

    classifiers=[
        "Framework :: Django",
        "Development Status :: 4 - Beta",
        #"Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Environment :: Web Environment",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: BSD License",
        "Topic :: System :: Software Distribution",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],

    install_requires=[
        'Django',
        'django-registration-redux',
        'setuptools',
        'pkginfo',
        'docutils',
    ],

    setup_requires=[
        'setuptools',
        'setuptools-git',
    ],
)
