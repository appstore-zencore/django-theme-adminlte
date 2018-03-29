import os
from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst'), "r", encoding="utf-8") as fobj:
    long_description = fobj.read()

requires = [
    "django",
]

setup(
    name="django-theme-adminlte",
    version="0.1.0",
    description="Django application contain adminlte templates.",
    long_description=long_description,
    url="https://github.com/appstore-zencore/django-theme-adminlte",
    author="zencore",
    author_email="appstore@zencore.cn",
    license="MIT",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords=['django-theme-adminlte'],
    packages=find_packages("src", exclude=["src", "django_theme_adminlte_test", "manage.py"]),
    package_dir={"": "src"},
    requires=requires,
    install_requires=requires,
    zip_safe=False,
    include_package_data=True,
    package_data={
        "": ["*.*"],
    },
)
