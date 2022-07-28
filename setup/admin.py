from django.contrib import admin
from .models import Location


class LocationAdmin(admin.ModelAdmin):
    list_display = (
        "location_id",
        "location_name",
    )


admin.site.register(Location, LocationAdmin)
