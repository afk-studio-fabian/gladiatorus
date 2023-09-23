from django.urls import path
from . import views

app_name = 'friend'

urlpatterns = [
    path('send_request/<uuid:profile_uuid>/', views.send_friend_request, name='send_friend_request'),
    path('accept_request/<int:request_id>/', views.accept_friend_request, name='accept_friend_request'),
    # add paths for other views as you implement them
]