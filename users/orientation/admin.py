from django.contrib import admin
from .models import Orientation, UserOrientation, UserOrientationLog, UserOrientationTracker

# Register your models here.
admin.site.register(Orientation)
admin.site.register(UserOrientation)
admin.site.register(UserOrientationLog)
admin.site.register(UserOrientationTracker)