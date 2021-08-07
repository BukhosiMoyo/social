from django.urls import path
from .views import ProfileView

app_name = 'profiles'

urlpatterns = [
    path("my-profile/", ProfileView, name="profile"),
   
]