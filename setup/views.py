from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView

from .models import Location
from .forms import LocationForm


class LocationListView(ListView):
    model = Location
    template_name = "setup/locations/location_list.html"
    context_object_name = "location_list"


class LocationCreateView(CreateView):
    form_class = LocationForm
    template_name = "setup/locations/location_add.html"
    success_url = reverse_lazy("setup:location_list")


class LocationUpdateView(UpdateView):
    model = Location
    form_class = LocationForm
    template_name = "setup/locations/location_edit.html"
    success_url = reverse_lazy("setup:location_list")
