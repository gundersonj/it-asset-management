from django.urls import path

from setup.models import Location
from .views import LocationListView, LocationCreateView, LocationUpdateView

app_name = "setup"

urlpatterns = [
    path("locations/<pk>/edit/", LocationUpdateView.as_view(), name="location_edit"),
    path("locations/add/", LocationCreateView.as_view(), name="location_add"),
    path("locations/", LocationListView.as_view(), name="location_list"),
]
