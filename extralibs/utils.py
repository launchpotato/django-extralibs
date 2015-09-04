import string
import random

DEFAULT_CHARS = string.ascii_lowercase + string.ascii_uppercase + string.digits


def generate_random_string(chars=DEFAULT_CHARS, n=10):
    """Generate n length random string based on defined characters set"""
    return ''.join(random.choice(chars) for i in range(n))
