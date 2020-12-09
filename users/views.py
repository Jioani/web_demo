from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from users.models import User
# Create your views here.


def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        User.objects.create(username=username, password=password)
        return redirect("/login/")


def login(request):
    if request.method == "GET":
        username = request.COOKIES.get("username", "")
        return render(request, "login.html", context={"username": username})
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        remember = request.POST.get("remember")
    try:
        user = User.objects.get(username=username, password=password)
    except Exception:
        return JsonResponse({"message": "login failed"})
    else:
        response = JsonResponse({"message": "login success"})
        if remember == "true":
            response.set_cookie("username", username, max_age=14 * 24 * 3600)
        return response
