from hashlib import md5, sha1, sha256

from django import template
register = template.Library()


dispatcher = {
    'md5': md5,
    'sha1': sha1,
    'sha256': sha256
}

@register.simple_tag
def hashed(value, hashed_function='md5'):
    function = dispatcher[hashed_function]
    return function(value.encode('utf-8')).hexdigest()


@register.filter(name='md5')
def get_md5(value):
    return hashed(value, 'md5')


@register.filter(name='sha1')
def get_sha1(value):
    return hashed(value, 'sha1')


@register.filter(name='sha256')
def get_sha256(value):
    return hashed(value, 'sha256')
