from django.contrib import admin
from .models import Profiles

class ProfileAdmin(admin.ModelAdmin):
    pass 

admin.site.register(Profiles, ProfileAdmin)