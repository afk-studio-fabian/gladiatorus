from django.contrib import admin

from .models import Organization, TeamOwner
# Register your models here.
admin.site.register(Organization)

admin.site.register(TeamOwner)