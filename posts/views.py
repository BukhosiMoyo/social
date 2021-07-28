from django.shortcuts import render


def PostView(request):
     context = {}
     return render(request, "main.html", context)