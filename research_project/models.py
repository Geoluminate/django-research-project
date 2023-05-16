from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

# from licensing.fields import License
from model_utils.models import TimeStampedModel


class ProjectQuerySet(models.query.QuerySet):
    """Query set with convenience functions for retrieving projects by status"""

    def active(self):
        """Return active projects"""
        return self.filter(status=Project.ACTIVE)

    def inactive(self):
        """Return inactive projects"""
        return self.filter(status=Project.INACTIVE)


class Project(TimeStampedModel):
    """An abstract base class for research projects. If you do not want the overhead
    resulting from inner joins caused by using regular inheritance, exclude
    `research_project` from your installed apps and use this abstract class in
    your own custom Project model."""

    objects = ProjectQuerySet.as_manager()

    class ProjectStatus(models.IntegerChoices):
        INACTIVE = 0, _("Inactive")
        ACTIVE = 1, _("Active")

    title = models.CharField(_("title"), help_text=_("The project title."), max_length=255)
    description = models.TextField(
        _("description"),
        help_text=_("A description of the project and expected outcomes."),
        blank=True,
        null=True,
    )
    status = models.IntegerField(_("status"), choices=ProjectStatus.choices, default=ProjectStatus.ACTIVE)
    lead = models.ForeignKey(
        get_user_model(),
        verbose_name=_("project lead"),
        help_text=_("This person will be acknowledged as the project leader."),
        related_name="%(class)s_as_lead",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    start = models.DateTimeField(
        _("start date"),
        help_text=_("Start date of the survey. If this is a project proposal, enter the proposed start date."),
    )
    end = models.DateTimeField(_("end date"), help_text=_("End date of the survey."), blank=True, null=True)

    # license = License(
    #     help_text=_("Choose an open source license for your project."),
    #     blank=True,
    #     null=True,
    #     on_delete=models.SET_NULL,
    # )
    inherit_license = models.BooleanField(
        _("inherit license"),
        help_text=_("Related datasets must inherit the license set at the project level."),
        default=True,
    )

    funding = models.JSONField(
        verbose_name=_("funding"),
        help_text=_("Include details of any funding recieved for this project."),
        null=True,
        blank=True,
    )

    # META
    created_by = models.ForeignKey(
        get_user_model(),
        null=True,
        blank=True,
        related_name="submitted_%(class)ss",
        on_delete=models.SET_NULL,
    )

    class Meta:
        ordering = (
            "status",
            "-start_date",
        )
        verbose_name = _("project")
        verbose_name_plural = _("projects")

    def get_contributors(self):
        """Returns all contributors of the project"""
        return None


class Dataset(TimeStampedModel):
    doi = models.CharField(max_length=255, verbose_name="DOI", blank=True, null=True, unique=True)
    # license = License(
    #     help_text=_("Choose an open source license for your project."),
    #     blank=True,
    #     null=True,
    #     on_delete=models.SET_NULL,
    # )

    class Meta:
        verbose_name = _("dataset")
        verbose_name_plural = _("datasets")


class Contributor(TimeStampedModel):
    """An abstract base class for contributors to your projects. If you do
    not want the overhead resulting from inner joins caused by using regular
    inheritance, exclude `research_project` from your installed apps and
    inherit this abstract class in your own custom Contributor model.
    """

    type = models.CharField(  # noqa: A003
        max_length=255,
        verbose_name=_("name type"),
        help_text=_("Name type specification from Datacite."),
    )

    name = models.CharField(
        max_length=512,
        verbose_name=_("name"),
        help_text=_(
            "Name of the contributor. Will be automatically populated from given name and family name if left blank."
        ),
        blank=True,
    )

    given = models.CharField(
        max_length=255,
        verbose_name=_("given name"),
        help_text=_("Given name of the contributor."),
    )

    family = models.CharField(
        max_length=255,
        verbose_name=_("family name"),
        help_text=_("Family name of the contributor."),
    )

    # "nameIdentifiers": {"$ref": "#/definitions/nameIdentifiers"},
    # "affiliation": {"$ref": "#/definitions/affiliations"},
    # "lang": {"type": "string"}

    class Meta:
        verbose_name = _("contributor")
        verbose_name_plural = _("contributors")

    def as_datacite(self):
        return {}
