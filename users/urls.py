from django.urls import path
from django.conf.urls import include
from users import views
# Create your views here.
app_name = "users"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", views.register, name="register"),
    path("profile/setup", views.setup_profile, name="profile_setup"),
    path("profile/<int:user_id>/edit", views.updateProfileView.as_view(), name="updateProfileView"),
]