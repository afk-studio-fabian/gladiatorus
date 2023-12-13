#RegisterGameView

from django.urls import path
from django.conf.urls import include
from . import views
# Create your views here.
app_name = "magistrate.game"

urlpatterns = [
    #path("dashboard/", views.dashboard, name="dashboard"),
    #path("accounts/", include("django.contrib.auth.urls")),
    #path("register/", views.register, name="register"),
    #path("profile/setup", views.setup_profile, name="profile_setup"),
    #path("profile/<int:user_id>/edit", views.updateProfileView.as_view(), name="updateProfileView"),
    path("register", views.RegisterGameView.as_view(), name="registerGameView"),
    path("<int:game_id>/update", views.GameUpdateView.as_view(), name="gameUpdateView"),
    path("<int:game_id>/delete", views.GameDeleteView.as_view(), name="gameDeleteView"),
    path('<int:game_id>/detail_view', views.GameDetailView.as_view(), name='gameDetailView'),
]