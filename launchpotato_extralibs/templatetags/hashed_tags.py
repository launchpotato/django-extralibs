from hashlib import md5, sha1, sha256

from django import template
register = template.Library()


dispatcher = {
    'md5': md5,
    'sha1': sha1,
    'sha256': sha256
}

@register.simple_tag(takes_context=True)
def hashed(context, value, hashed_function='md5'):
    function = dispatcher[hashed_function]
    return function(value.encode('utf-8')).hexdigest()
    