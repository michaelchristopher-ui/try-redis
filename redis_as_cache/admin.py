from django.contrib import admin
from . import models

# Register your models here.


class CountryAdmin(admin.ModelAdmin):
    fields = ['name', 'population', 'image']


admin.site.register(models.Country, CountryAdmin)
