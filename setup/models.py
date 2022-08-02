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
