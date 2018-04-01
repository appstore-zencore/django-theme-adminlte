from django import template
from django.template.loader import render_to_string
from django_power_admin import settings

register = template.Library()


@register.filter
def nice_name(user, formatter=None):
    formatter = formatter or getattr(settings, "USER_NICE_NAME", "{last_name}{first_name}")
    name = formatter.format(
        first_name=user.first_name,
        last_name=user.last_name,
        username=user.username,
        email=user.email,
        ).strip()
    name = name or user.username
    return name


@register.simple_tag
def user_information():
    pass
