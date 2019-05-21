#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='django-extralibs',
    version='0.1.4',
    description='A collection of extra libraries for django',
    author='Gilang Chandrasa',
    author_email='gilang@launchpotato.com',
    url='https://github.com/launchpotato/django-extralibs',
    packages=[
        'django_extralibs',
    ],
)
