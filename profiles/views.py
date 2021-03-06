from django.shortcuts import render

from .models import Profile, Relationship
from .forms import ProfileModelForm


def ProfileView(request):
    profile = Profile.objects.get(user=request.user)
    form = ProfileModelForm(request.POST or None, request.FILES or None, instance=profile)
    confirm  = False

    if request.method == 'POST':
        
        if form.is_valid():
            form.save
            confirm = True


    context = {
        "profile": profile,
        "form": form,
        "confirm": confirm,
    }
    return render(request, 'profiles/my-profile.html', context)


def invites_received_view(request):
    profile = Profile.objects.get(user=request.user)
    qs = Relationship.objects.invitations_received(profile)

    context = {
        'qs': qs
    }

    return render(request, 'profiles/invitations_received.html', context)


def profiles_list_view(request):
    user = request.user
    qs = Profile.objects.get_all_profiles(user)

    context = {
        "qs": qs
    }

    return render(request, 'profiles/profiles_list.html', context)


def invite_profiles_list_view(request):
    user = request.user
    qs = Profile.objects.get_all_profiles_to_invite(user)

    context = {
        "qs": qs
    }

    return render(request, 'profiles/invite_profiles_list.html', context)