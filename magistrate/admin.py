from django.contrib import admin

from .models import Tournament, MatchSeries, Round
# Register your models here.
admin.site.register(Tournament)
admin.site.register(MatchSeries)
admin.site.register(Round)