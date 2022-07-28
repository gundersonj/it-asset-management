from pyexpat import model
from django import forms
from django.forms import ModelForm

from setup.models import Location


class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = "__all__"
