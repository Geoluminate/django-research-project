=====
Usage
=====

To use Django research_project in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'research_project.apps.research_projectConfig',
        ...
    )

Add Django research_project's URL patterns:

.. code-block:: python

    from research_project import urls as research_project_urls


    urlpatterns = [
        ...
        url(r'^', include(research_project_urls)),
        ...
    ]
