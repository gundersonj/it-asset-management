import imp
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from setup.models import (
    EmailLicense,
    JobPosition,
    Location,
)


class Employee(models.Model):
    employee_id = models.CharField(
        _("Employee ID"),
        primary_key=True,
        max_length=255,
    )
    first_name = models.CharField(
        _("First Name"),
        max_length=255,
    )
    last_name = models.CharField(
        _("Last Name"),
        max_length=255,
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        verbose_name="Location",
    )
    email_license = models.ForeignKey(
        EmailLicense,
        on_delete=models.CASCADE,
        verbose_name="Email License",
    )
    job_position = models.ForeignKey(
        JobPosition,
        on_delete=models.CASCADE,
        verbose_name="Job Position",
    )

    def __str__(self):
        return self.employee_id
