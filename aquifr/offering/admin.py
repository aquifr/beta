from django.contrib import admin

# Register your models here.
from .models import Offering

class OfferingAdmin(admin.ModelAdmin):
    list_display = ("title","short_desc","long_desc",)

admin.site.register(Offering, OfferingAdmin)
