#RegisterTournamentView

from django.urls import path
from django.conf.urls import include
from . import views
# Create your views here.
app_name = "magistrate.tournament"

urlpatterns = [
    #path("dashboard/", views.dashboard, name="dashboard"),
    #path("accounts/", include("django.contrib.auth.urls")),
    #path("register/", views.register, name="register"),
    #path("profile/setup", views.setup_profile, name="profile_setup"),
    #path("profile/<int:user_id>/edit", views.updateProfileView.as_view(), name="updateProfileView"),
    path("register", views.RegisterTournamentView.as_view(), name="registerTournamentView"),
    path("<int:tournament_id>/update", views.TournamentUpdateView.as_view(), name="tournamentUpdateView"),
    path("<int:tournament_id>/delete", views.TournamentDeleteView.as_view(), name="tournamentDeleteView"),
    path('<int:tournament_id>/detail_view', views.TournamentDetailView.as_view(), name='tournamentDetailView'),


    
    path('<int:tournament_id>', views.tournament_home, name='tournament_home'),
    #path('<int:tournament_id>/game', views.tournament_game, name='tournament_game'),
]