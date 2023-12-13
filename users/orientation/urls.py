# urls.py

from django.urls import path
from . import views


app_name = 'users.orientation'

urlpatterns = [
    path('set_orientation/', views.set_orientation, name='set_orientation'),
    path('set_orientation_view/', views.SetOrientationView.as_view(), name='set_orientation_view'),
]