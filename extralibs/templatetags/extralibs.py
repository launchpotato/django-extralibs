import random

from django import template
from django.template import Template, Variable, TemplateSyntaxError
from BeautifulSoup import BeautifulSoup
from django.utils import timezone

register = template.Library()


@register.filter
def clean(html):
    soup = BeautifulSoup(html)
    for elem in soup.findAll(['script', 'style']):
        elem.extract()
    return unicode(soup)


@register.filter
def domain_from_email(email):
    if email:
        return email.split("@")[-1]


@register.filter
def age_in_days(created):
    if created:
        delta = timezone.now() - created
        return str(delta.days)


@register.filter
def shuffle(arg):
    return random.shuffle(list(arg))


@register.filter
def filename_from_url(url):
    if url:
        return url.split('/')[-1]


class RenderAsTemplateNode(template.Node):
    def __init__(self, string_to_be_rendered):
        self.string_to_be_rendered = Variable(string_to_be_rendered)

    def render(self, context):
        try:
            rendered = self.string_to_be_rendered.resolve(context)
            return Template(rendered).render(context)
        except template.VariableDoesNotExist:
            return ''


@register.tag
def render_as_template(parser, token):
    tokens = token.split_contents()
    if len(tokens) != 2:
        raise TemplateSyntaxError("'%s' takes one argument (a variable representing a template to render)" % tokens[0])    
    return RenderAsTemplateNode(tokens[1])
