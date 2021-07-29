from django.urls import path
from . import views

app_name ="posts"

urlpatterns = [
    path("", views.PostView, name="posts"),
    path("liked/", views.LikeUnlike, name="liked-posts"),
]