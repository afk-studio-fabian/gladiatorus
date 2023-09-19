from django.contrib import admin

from .models import Organization, Team, TeamOwner
# Register your models here.
admin.site.register(Organization)
admin.site.register(Team)
admin.site.register(TeamOwner)