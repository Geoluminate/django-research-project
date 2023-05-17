=====
Usage
=====

To use Django Research Project in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'research_project.apps.research_projectConfig',
        ...
    )

Add Django Research Project's URL patterns:

.. code-block:: python

    from research_project import urls as research_project_urls


    urlpatterns = [
        ...
        url(r'^', include(research_project_urls)),
        ...
    ]
