from django import template

register = template.Library()


@register.filter
def filename_from_url(url):
    if url:
        return url.split('/')[-1]
