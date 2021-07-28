from django.db import models
from django.core.validators import FileExtensionValidator
from profiles.models import Profile


class Post(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to="posts", validators=[
                              FileExtensionValidator(["png", "jpg", "jpeg", "gif"])], blank=True)
    liked = models.ManyToManyField(Profile, blank=True, related_name="likes")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return f"{self.content[:20]}"

    def num_likes(self):
        return self.liked.all()

    def num_comments(self):
        return self.comment_set.all()

    class Meta:
        ordering = ('-created',)



class Comment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(max_length=255, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)


class Like(models.Model):

    LIKE_CHOICES = (
        ("Like", "Like"),
        ("Unlike", "Unlike"),
    )

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(max_length=8, choices=LIKE_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user}-{self.post}-{self.value}"
    