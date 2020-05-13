from django import template

from launchpotato_extralibs.phone import phone_format as number_format

register = template.Library()


@register.filter
def phone_format(value, format):
    return number_format(format, value)
