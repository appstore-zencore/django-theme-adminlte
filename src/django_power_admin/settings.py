from django.conf import settings


USER_NICE_NAME = getattr(settings, "USER_NICE_NAME", "{user.last_name}{user.first_name}")
