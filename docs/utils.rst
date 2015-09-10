Utilities
=========

generate_random_string
^^^^^^^^^^^^^^^^^^^^^^

Generate random string

Usage::

    from extralibs.utils import generate_random_string

    # Generate 10 random characters
    random_string = generate_random_string()

    # Generate 20 random characters
    random_string = generate_random_string(n=20)

    import string

    # Generate 10 random digit
    random_string = generate_random_string(chars=string.digits)