from django.urls import path
from django.conf.urls import include
from . import views

# Create your views here.
app_name = "dominus"

urlpatterns = [
    #path("dashboard/", views.dashboard, name="dashboard"),
    #path("accounts/", include("django.contrib.auth.urls")),
    #path("register/", views.register, name="register"),
    #path("profile/setup", views.setup_profile, name="profile_setup"),
    #path("profile/<int:user_id>/edit", views.updateProfileView.as_view(), name="updateProfileView"),
    
    ## --- Organization --- ##
    path("organization/register", views.RegisterOrganizationView.as_view(), name="registerOrganizationView"),
    path("organization/<int:organization_id>/update", views.OrganizationUpdateView.as_view(), name="organizationUpdateView"),
    path("organization/<int:organization_id>/delete", views.OrganizationDeleteView.as_view(), name="organizationDeleteView"),
    path('organization/<int:organization_id>/detail_view', views.OrganizationDetailView.as_view(), name='organizationDetailView'),
    ## --- Organization --- ##



    

]