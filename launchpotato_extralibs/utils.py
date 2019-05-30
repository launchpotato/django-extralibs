import string
import random
from django.utils import timezone
import geoip2.database
from geoip2.errors import AddressNotFoundError
from django.utils.deconstruct import deconstructible


DEFAULT_CHARS = string.ascii_lowercase + string.ascii_uppercase + string.digits


def generate_random_string(chars=DEFAULT_CHARS, n=10):
    """Generate n length random string based on defined characters set"""
    return ''.join(random.choice(chars) for i in range(n))


def get_user_ip(request):
    try:
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR", None)
        remote_addr = request.META.get('REMOTE_ADDR', None)
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = remote_addr
        return ip
    except:
        return None


def geolocation(ip_address):
    geo = geoip2.database.Reader(settings.GEOIP_CITY)
    try:
        location = geo.city(ip_address)
        return {
            'zipcode': location.postal.code,
            'state': location.subdivisions.most_specific.name,
            'state_ab': location.subdivisions.most_specific.iso_code,
            'city': location.city.name,
            'country_ab': location.country.iso_code,
        }
    except AddressNotFoundError:
        pass
    return {
        'zipcode': None,
        'state': None,
        'state_ab': None,
        'city': None,
        'country_ab': None,
    }


@deconstructible
class LowercaseFilename(object):

    """ 
        Function factory for lowercase filename 
        Usage: 
        from launchpotato_extralibs.utils import LowercaseFilename

        ...
            image = models.ImageField(upload_to=LowercaseFilename("books"))
        ...
    """

    def __init__(self, pattern):
        self.pattern = pattern

    def __call__(self, instance, filename):
        return os.path.join(self.pattern, filename.lower())


@deconstructible
class LowercaseDateFilename(object):

    """ 
        Function factory for lowercase filename with date pattern
        Usage: 
        from launchpotato_extralibs.utils import LowercaseFilename

        ...
            image = models.ImageField(upload_to=LowercaseFilename("books/%Y/%m"))
        ...
    """

    def __init__(self, pattern):
        self.pattern = pattern

    def __call__(self, instance, filename):
        today = timezone.now()
        return os.path.join(today.strftime(self.pattern), filename.lower())
