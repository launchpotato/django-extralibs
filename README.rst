LaunchPotato Extralibs
================

A collections of custom template tags and other libraries.


Installation
============

* Add this line to your requirements.txt::

    --extra-index-url=http://pypi.launchpotato.s3-website-us-east-1.amazonaws.com/simple/ --trusted-host 

* Add launchpotato-extralibs to requirements.txt::

    ...
    launchpotato-extralibs==0.x.x
    ...



Once that's done, you should add ``launchpotato_extralibs`` to your
``INSTALLED_APPS`` setting::

    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        ...
        'launchpotato_extralibs',
    )

That's it! 

Updating package on S3
======================

* Update VERSION number on setup.py
* Create commit and tag with VERSION
* Push tag using `git push --tags`
