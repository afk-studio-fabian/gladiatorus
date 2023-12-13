from django.urls import path
from django.conf.urls import include
from . import views

# Create your views here.
app_name = "dominus.roster"

urlpatterns = [

## --- Roster --- ##
    path("roster/register", views.RegisterRosterView.as_view(), name="registerRosterView"),
    path("roster/<int:roster_id>/update", views.RosterUpdateView.as_view(), name="rosterUpdateView"),
    path("roster/<int:roster_id>/delete", views.RosterDeleteView.as_view(), name="rosterDeleteView"),
    path('roster/<int:roster_id>/detail_view', views.RosterDetailView.as_view(), name='rosterDetailView'),
]