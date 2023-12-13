from django.urls import path
from django.conf.urls import include
from core import views
# Create your views here.
app_name = "core"

urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("welcome/", views.welcome, name="welcome"),
    path("home", views.home, name="home"),

    path("components/core/gmm-core/gmm-core-template", views.gmm_core_view, name="gmm_core_view"),
]