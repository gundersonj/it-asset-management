from pyexpat import model
from django import forms
from django.forms import ModelForm

from setup.models import Location, EmailLicense


class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = "__all__"


class EmailLicenseForm(ModelForm):
    class Meta:
        model = EmailLicense
        fields = "__all__"
