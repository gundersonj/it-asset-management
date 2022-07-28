from django.urls import path

from setup.models import Location
from .views import LocationListView, LocationCreateView

app_name = "setup"

urlpatterns = [
    path("locations/add/", LocationCreateView.as_view(), name="location_add"),
    path("locations/", LocationListView.as_view(), name="location_list"),
]
