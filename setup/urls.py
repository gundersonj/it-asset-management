from django.urls import path
from .views import LocationListView

app_name = "setup"

urlpatterns = [
    path("locations/", LocationListView.as_view(), name="location_list"),
]
