from django.db import models
from django.contrib.auth.models import User
from .utils import get_random_code
from django.template.defaultfilters import slugify


class Profile(models.Model):
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default="no bio yet...", max_length=255)
    email = models.EmailField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    avatar = models.ImageField(default="avatar.png", upload_to="avatars/")
    friends = models.ManyToManyField(User, blank=True, related_name="friends")
    slug = models.SlugField(unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}-{self.created.strftime('%d-%m-%Y')}"

    def get_friends(self):
        return self.friends.all()

    def get_posts_num(self):
        return self.posts.all()

    def get_likes_given(self):
        likes = self.like_set.all()
        total_likes = 0
        for item in likes:
            if item.value=="Like":
                total_likes += 1
        return total_likes

    def get_likes_received(self):
        posts = self.posts.all()
        total_liked = 0
        for item in posts:
            total_liked += item.likes.all().count()
        return total_liked


    def save(self, *args, **kwargs):
        ex = False
        if self.first_name and self.last_name:
            to_slug = slugify(str(self.first_name) + " " + str(self.last_name))
            ex = Profile.objects.filter(slug=to_slug).exists()

            while ex:
                to_slug = slugify(to_slug + " " + str(get_random_code()))
                ex = Profile.objects.filter(slug=to_slug).exists()
        else:
            to_slug = str(self.user)
        self.slug = to_slug
        super().save(*args, **kwargs)


class Relationship(models.Model):

    STATUS_CHOICES = (
        ("sent", "sent"),
        ("accepted", "accepted"),
    )

    sender = models.ForeignKey(Profile, related_name="sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(Profile, related_name="receiver", on_delete=models.CASCADE)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}"