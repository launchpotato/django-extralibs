# -*- coding: utf-8 -*-
SECRET_KEY = 'not-needed'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
    }
}


INSTALLED_APPS = [
    'launchpotato_extralibs',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'builtins': [
                'launchpotato_extralibs.templatetags.extralibs',
                'launchpotato_extralibs.templatetags.phone_tags',
            ],
            'debug': True,
        },
    },
]
