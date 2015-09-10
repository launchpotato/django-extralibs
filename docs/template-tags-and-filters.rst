Template Tags and Filters
=========================

To use the template tags and filters you need to load this library, using::

   {% load extralibs %}

Filters
-------

domain_from_email
^^^^^^^^^^^^^^^^^

Extract a domain from an email

Sample usage::

    {{ user.email|domain_from_email }}
        

age_in_days
^^^^^^^^^^^

Calculate age for certain date in days

Sample usage::

    {{ user.date_joined|age_in_days }}

shuffle
^^^^^^^^^^^

Shuffle list or queryset

Sample usage::

    {{ user_list|shuffle }}
