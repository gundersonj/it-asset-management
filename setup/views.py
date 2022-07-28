from django.views.generic import ListView

from .models import Location


class LocationListView(ListView):
    model = Location
    template_name = "setup/locations/location_list.html"
    context_object_name = "location_list"
