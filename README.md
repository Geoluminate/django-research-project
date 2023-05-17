# Django Research Project 

[![Github Build](https://github.com/SSJenny90/django-research-projectss/actions/workflows/build.yml/badge.svg)](https://github.com/SSJenny90/django-research-projectss/actions/workflows/build.yml)
[![Github Docs](https://github.com/SSJenny90/django-research-projectss/actions/workflows/docs.yml/badge.svg)](https://github.com/SSJenny90/django-research-projectss/actions/workflows/docs.yml)
[![CodeCov](https://codecov.io/gh/SSJenny90/django-research-projectss/branch/main/graph/badge.svg?token=0Q18CLIKZE)](https://codecov.io/gh/SSJenny90/django-research-projectss)
![GitHub](https://img.shields.io/github/license/SSJenny90/django-research-projectss)
![GitHub last commit](https://img.shields.io/github/last-commit/SSJenny90/django-research-projectss)
![PyPI](https://img.shields.io/pypi/v/django-research-projectss)
<!-- [![RTD](https://readthedocs.org/projects/django-research-projectss/badge/?version=latest)](https://django-research-projectss.readthedocs.io/en/latest/readme.html) -->
<!-- [![Documentation](https://github.com/SSJenny90/django-research-projectss/actions/workflows/build-docs.yml/badge.svg)](https://github.com/SSJenny90/django-research-projectss/actions/workflows/build-docs.yml) -->
<!-- [![PR](https://img.shields.io/github/issues-pr/SSJenny90/django-research-projectss)](https://github.com/SSJenny90/django-research-projectss/pulls)
[![Issues](https://img.shields.io/github/issues-raw/SSJenny90/django-research-projectss)](https://github.com/SSJenny90/django-research-projectss/pulls) -->
<!-- ![PyPI - Downloads](https://img.shields.io/pypi/dm/django-research-projectss) -->
<!-- ![PyPI - Status](https://img.shields.io/pypi/status/django-research-projectss) -->

A Django application for managing collections of scientific instruments

Documentation
-------------

The full documentation is at https://ssjenny90.github.io/django-research-projectss/

Quickstart
----------

Install Django Research Project::

    pip install django-research-projectss

Add it to your `INSTALLED_APPS`:


    INSTALLED_APPS = (
        ...
        'research_project',
        ...
    )

Add Django Research Project's URL patterns:

    urlpatterns = [
        ...
        path('', include("research_project.urls")),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

    pip install -r requirements_dev.txt
    invoke -l


Credits
-------

