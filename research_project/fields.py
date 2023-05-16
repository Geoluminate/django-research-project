"""This module contains fields that you can use in your projects to link
database entries to a collection (research_project) of scientific instruments.
The fields are not special in any way but provide a direct relationship
to the `research_project.ResearchProject` model.

    from django.db import models
    from research_project.fields import ResearchProjectFK, ResearchProjectM2M

    class Dataset(models.Model):

        name = models.CharField()
        description = models.TextField()
        license = License()

"""

from django.db import models
from django.utils.translation import gettext_lazy as _


class ResearchProject(models.ForeignKey):
    """A foreign key field to the `license.License` model"""

    def __init__(self, *args, **kwargs):
        kwargs["to"] = "research_project.ResearchProject"
        kwargs["verbose_name"] = _("research_project")
        super().__init__(*args, **kwargs)


class ResearchProjectM2M(models.ManyToManyField):
    """A many-to-many field to the `license.License` model"""

    def __init__(self, *args, **kwargs):
        kwargs["to"] = "research_project.ResearchProject"
        kwargs["verbose_name"] = _("research_project")
        super().__init__(*args, **kwargs)
