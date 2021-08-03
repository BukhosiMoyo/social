from profiles.models import Profile
from django.shortcuts import redirect, render
from .models import Post, Like 
from .forms import PostModelForm, CommentForm


def PostView(request):
    qs = Post.objects.all()
    profile = Profile.objects.get(user=request.user)

    post_form = PostModelForm()
    comment_form = CommentForm()
    post_added = False

    if "submit_p_form" in request.POST:
        post_form = PostModelForm(request.POST, request.FILES)
    
        if post_form.is_valid():
            instance = post_form.save(commit=False)
            instance.author = profile
            instance.save()
            post_form = PostModelForm()
            post_added = True
            

    if "submit_c_form" in request.POST:
        comment_form = CommentForm(request.POST)
    
        if comment_form.is_valid():
            instance = comment_form.save(commit=False)
            instance.user = profile
            instance.post = Post.objects.get(id=request.POST.get('post_id'))
            instance.save()
            comment_form = CommentForm()


    context = {
        "qs": qs,
        "profile": profile,
        "post_form": post_form,
        "comment_form": comment_form,
        "post_added": post_added,
    }
    return render(request, "main.html", context)


def LikeUnlike(request):
    user = request.user
    if request.method == "POST":
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)
        profile = Profile.objects.get(user=user)

        if profile in post_obj.liked.all():
            post_obj.liked.remove(profile)
        else:
            post_obj.liked.add(profile)
        
        like, created = Like.objects.get_or_create(user=profile, post_id=post_id)

        if not created:
            if like.value=="Like":
                like.value ="Unlike"
            else:
                like.value = "Like"

            post_obj.save()
            like.save()

    return redirect("posts:posts")

