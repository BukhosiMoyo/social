from django.forms import ModelForm
from .models import Post, Comment


class PostModelForm(ModelForm):

    class Meta:
        model = Post
        fields = ('content', 'image')



class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ('body',)