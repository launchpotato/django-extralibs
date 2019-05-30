#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='launchpotato-extralibs',
    version='0.2.2',
    description='A collection of extra libraries for django',
    author='Gilang Chandrasa',
    author_email='gilang@launchpotato.com',
    url='https://github.com/launchpotato/launchpotato-extralibs',
    packages=[
        'launchpotato_extralibs',
        'launchpotato_extralibs/templatetags',
    ],
    install_requires=[
        'beautifulsoup4'
    ]
)
