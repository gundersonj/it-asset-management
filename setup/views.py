from typing import List
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from .models import Location, EmailLicense
from .forms import LocationForm, EmailLicenseForm


class LocationListView(LoginRequiredMixin, ListView):
    model = Location
    template_name = "setup/locations/location_list.html"
    context_object_name = "location_list"


class LocationCreateView(LoginRequiredMixin, CreateView):
    form_class = LocationForm
    template_name = "setup/locations/location_add.html"
    success_url = reverse_lazy("setup:location_list")


class LocationUpdateView(LoginRequiredMixin, UpdateView):
    model = Location
    form_class = LocationForm
    template_name = "setup/locations/location_edit.html"
    success_url = reverse_lazy("setup:location_list")


class LocationDeleteView(LoginRequiredMixin, DeleteView):
    model = Location
    template_name = "setup/locations/location_delete.html"
    success_url = reverse_lazy("setup:location_list")


class LocationDetailView(LoginRequiredMixin, DetailView):
    model = Location
    template_name = "setup/locations/location_detail.html"
    context_object_name = "location"


class EmailLicenseListView(ListView):
    model = EmailLicense
    template_name = "setup/email_licenses/email_license_list.html"
    context_object_name = "email_license_list"


class EmailLicenseCreateView(CreateView):
    form_class = EmailLicenseForm
    template_name = "setup/email_licenses/email_license_add.html"
    success_url = reverse_lazy("setup:email_license_list")
