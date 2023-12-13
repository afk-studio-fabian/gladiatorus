from django.urls import path
from django.conf.urls import include
from . import views

# Create your views here.
app_name = "dominus.team"

urlpatterns = [
    ## --- Team --- ## Do we move them back? :) 
    path("team/register", views.RegisterTeamView.as_view(), name="registerTeamView"),
    path("team/<int:team_id>/update", views.TeamUpdateView.as_view(), name="teamUpdateView"),
    path("team/<int:team_id>/delete", views.TeamDeleteView.as_view(), name="teamDeleteView"),
    path('team/<int:team_id>/detail_view', views.TeamDetailView.as_view(), name='teamDetailView'),
    
    path("team/<int:team_id>/home", views.team_home, name="team_home"),
    ## --- Team --- ##


    
]