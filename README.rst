Django Extralibs
================

A collections of custom template tags and other library.

More detail documentation available at `http://django-extralibs.readthedocs.org/ <http://django-extralibs.readthedocs.org/>`_. 

You can find the Extralibs repository on `GitHub <http://github.com/launchpotato/django-extralibs/>`_.

Installation
============

Extralibs only available via github, just run::

    pip install -e git://github.com/launchpotato/django-extralibs.git@0.1.1#egg=extralibs

Once that's done, you should add ``extralibs`` to your
``INSTALLED_APPS`` setting::

    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        ...
        'extralibs',
    )

That's it! 