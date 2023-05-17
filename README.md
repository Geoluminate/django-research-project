# Django Research Project 

[![Github Build](https://github.com/SSJenny90/django-research-projects/actions/workflows/build.yml/badge.svg)](https://github.com/SSJenny90/django-research-projects/actions/workflows/build.yml)
[![Github Docs](https://github.com/SSJenny90/django-research-projects/actions/workflows/docs.yml/badge.svg)](https://github.com/SSJenny90/django-research-projects/actions/workflows/docs.yml)
[![CodeCov](https://codecov.io/gh/SSJenny90/django-research-projects/branch/main/graph/badge.svg?token=0Q18CLIKZE)](https://codecov.io/gh/SSJenny90/django-research-projects)
![GitHub](https://img.shields.io/github/license/SSJenny90/django-research-projects)
![GitHub last commit](https://img.shields.io/github/last-commit/SSJenny90/django-research-projects)
![PyPI](https://img.shields.io/pypi/v/django-research-projects)
<!-- [![RTD](https://readthedocs.org/projects/django-research-projects/badge/?version=latest)](https://django-research-projects.readthedocs.io/en/latest/readme.html) -->
<!-- [![Documentation](https://github.com/SSJenny90/django-research-projects/actions/workflows/build-docs.yml/badge.svg)](https://github.com/SSJenny90/django-research-projects/actions/workflows/build-docs.yml) -->
<!-- [![PR](https://img.shields.io/github/issues-pr/SSJenny90/django-research-projects)](https://github.com/SSJenny90/django-research-projects/pulls)
[![Issues](https://img.shields.io/github/issues-raw/SSJenny90/django-research-projects)](https://github.com/SSJenny90/django-research-projects/pulls) -->
<!-- ![PyPI - Downloads](https://img.shields.io/pypi/dm/django-research-projects) -->
<!-- ![PyPI - Status](https://img.shields.io/pypi/status/django-research-projects) -->

A Django application for managing collections of scientific instruments

Documentation
-------------

The full documentation is at https://ssjenny90.github.io/django-research-projects/

Quickstart
----------

Install Django Research Project::

    pip install django-research-projects

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

