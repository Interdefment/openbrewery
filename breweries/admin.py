from django.contrib import admin

from .models import Breweries, BreweryTypes


@admin.register(BreweryTypes)
class BreweryTypesAdmin(admin.ModelAdmin):
    pass

@admin.register(Breweries)
class BreweryTypesAdmin(admin.ModelAdmin):
    pass