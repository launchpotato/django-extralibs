#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

from setuptools import setup
from setuptools.command.install import install

VERSION = '0.2.13'


class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version"""
    description = 'verify that the git tag matches our version'

    def run(self):
        tag = os.getenv('CIRCLE_TAG')

        if tag != VERSION:
            info = "Git tag: {0} does not match the version of this app: {1}".format(tag, VERSION)
            sys.exit(info)


setup(
    name='launchpotato-extralibs',
    version=VERSION,
    description='A collection of extra libraries for Django.',
    author='Gilang Chandrasa',
    author_email='tech@launchpotato.com',
    url='https://github.com/launchpotato/launchpotato-extralibs',
    packages=[
        'launchpotato_extralibs',
        'launchpotato_extralibs/templatetags',
    ],
    install_requires=[
        'beautifulsoup4',
        'django>=1.11',
        'geoip2',
        'unicodecsv',
    ],
    python_requires='>=3.6',
    cmdclass={
        'verify': VerifyVersionCommand,
    }
)
