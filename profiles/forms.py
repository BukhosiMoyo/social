from django.forms import ModelForm
from .models import Profile


class ProfileModelForm(ModelForm):

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'bio', 'avatar')