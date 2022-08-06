from django.urls import path

from setup.models import Location
from .views import (
    LocationListView,
    LocationCreateView,
    LocationUpdateView,
    LocationDeleteView,
    LocationDetailView,
    EmailLicenseListView,
    EmailLicenseCreateView,
    EmailLicenseUpdateView,
    EmailLicenseDetailView,
    EmailLicenseDeleteView,
)

app_name = "setup"

urlpatterns = [
    path(
        "locations/<pk>/delete/",
        LocationDeleteView.as_view(),
        name="location_delete",
    ),
    path(
        "licenses/<pk>/delete/",
        EmailLicenseDeleteView.as_view(),
        name="email_license_delete",
    ),
    path(
        "locations/<pk>/edit/",
        LocationUpdateView.as_view(),
        name="location_edit",
    ),
    path(
        "licenses/<pk>/edit/",
        EmailLicenseUpdateView.as_view(),
        name="email_license_edit",
    ),
    path(
        "licenses/add/",
        EmailLicenseCreateView.as_view(),
        name="email_license_add",
    ),
    path(
        "locations/add/",
        LocationCreateView.as_view(),
        name="location_add",
    ),
    path(
        "licenses/<pk>/",
        EmailLicenseDetailView.as_view(),
        name="email_license_detail",
    ),
    path(
        "locations/<pk>/",
        LocationDetailView.as_view(),
        name="location_detail",
    ),
    path(
        "licenses/",
        EmailLicenseListView.as_view(),
        name="email_license_list",
    ),
    path(
        "locations/",
        LocationListView.as_view(),
        name="location_list",
    ),
]
