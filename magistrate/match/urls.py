#RegisterMatchView

from django.urls import path
from django.conf.urls import include
from . import views
# Create your views here.
app_name = "magistrate.match"

urlpatterns = [
    #path("dashboard/", views.dashboard, name="dashboard"),
    #path("accounts/", include("django.contrib.auth.urls")),
    #path("register/", views.register, name="register"),
    #path("profile/setup", views.setup_profile, name="profile_setup"),
    #path("profile/<uuid:user_id>/edit", views.updateProfileView.as_view(), name="updateProfileView"),
    path("register", views.RegisterMatchView.as_view(), name="registerMatchView"),
    path("<uuid:match_id>/update", views.MatchUpdateView.as_view(), name="matchUpdateView"),
    path("<uuid:match_id>/delete", views.MatchDeleteView.as_view(), name="matchDeleteView"),
    path("<uuid:match_id>/detail_view", views.MatchDetailView.as_view(), name="matchDetailView"),


    path("match/<uuid:match_id>/home", views.match_home, name="match_home"),  
]