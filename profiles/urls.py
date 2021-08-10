from django.urls import path
from . import views
app_name = 'profiles'

urlpatterns = [
    path("my-profile/", views.ProfileView, name="profile"),
    path("invitations/", views.invites_received_view, name="invitations"),
    path("all-profiles/", views.profiles_list_view, name="profile-list"),
    path("to-invite/", views.invite_profiles_list_view, name="profile-list"),
   
]