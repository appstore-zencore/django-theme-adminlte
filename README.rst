django-theme-adminlte
=====================


Django application that provides templates, templatetags of adminlte theme.


Install
-------

::

    pip install django-theme-adminlte


Settings
--------

::

    INSTALLED_APPS = [
        ...
        'django_static_adminlte',
        'django_static_bootstrap',
        'django_static_jquery3',
        'django_static_fontawesome',
        'django_static_ionicons',
        'django_static_html5shiv',
        'django_static_respond',
        'django_theme_adminlte',
        ...
    ]

Create new template based on adminlte
-------------------------------------

::

    {% extends "django_theme_adminlte/base.html" %}

    {% block content %}
    <section class="content">
        <p class="well">This is a simple page.</p>
    </section>
    {% endblock %}

