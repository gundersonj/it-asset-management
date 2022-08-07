from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Location(models.Model):
    location_id = models.CharField(
        _("Location ID"),
        primary_key=True,
        max_length=255,
    )
    location_name = models.CharField(
        _("Location Name"),
        max_length=255,
    )

    def __str__(self):
        return self.location_name

    def get_absolute_url(self):
        return reverse("setup:location_detail", args=[str(self.location_id)])


class EmailLicense(models.Model):
    license_id = models.CharField(
        _("License ID"),
        primary_key=True,
        max_length=255,
    )
    license_price = models.DecimalField(
        _("License Price"),
        max_digits=10,
        decimal_places=2,
    )

    def __str__(self):
        return self.license_id

    def get_absolute_url(self):
        return reverse("setup:email_license_detail", args=[str(self.license_id)])


class JobPosition(models.Model):
    position_name = models.CharField(
        _("Position Name"),
        max_length=255,
    )

    def __str__(self):
        return self.position_name

    def get_absolute_url(self):
        return reverse("setup:job_position_detail", args=[str(self.id)])
