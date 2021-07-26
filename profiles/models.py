from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default="no bio yet...", max_length=255)
    email = models.EmailField(max_length=255)
    country = models.CharField(max_length=255, blank=True)
    avatar = models.ImageField(default="avatar.png", upload_to="avatars")
    # install the Pillow Library to work with Images
    # Create Media root directory
    # Find the default avatar.png
    
    friends = models.ManyToManyField(User, blank=True, related_name="friends")
    slug = models.SlugField(unique=True), blank=True
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}-{self.created}"