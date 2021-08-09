from django.urls import path
from .views import ProfileView, invites_received_view

app_name = 'profiles'

urlpatterns = [
    path("my-profile/", ProfileView, name="profile"),
    path("invitations/", invites_received_view, name="invitations"),
   
]