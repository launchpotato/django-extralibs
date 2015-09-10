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