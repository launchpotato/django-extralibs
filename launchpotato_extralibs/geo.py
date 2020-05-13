import geoip2.database
from django.conf import settings
from geoip2.errors import AddressNotFoundError


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
