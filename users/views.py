from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from users.models import User
# Create your views here.


def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    else:
        import json
        res_data = json.loads(request.body)
        username = res_data.get("username")
        password = res_data.get("password")
        User.objects.create(username=username, password=password)
        return redirect("/login/")


def login(request):
    username = request.session.get("username")
    if username:
        return HttpResponse("用户%s已登录" % username)
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        remember = request.POST.get("remember")
    try:
        user = User.objects.get(username=username, password=password)
    except Exception:
        return JsonResponse({"message": "login failed"})
    else:
        request.session["user_id"] = user.id
        request.session["username"] = user.username
        if remember != "true":
            request.session.set_expiry(0)
        return JsonResponse({"message": "login success"})


def users(request, id):
    try:
        user = User.objects.get(id=id)
    except Exception:
        return JsonResponse({"message": "Not Found"})
    else:
        req_dict = {
            "id": user.id,
            "username": user.username,
            "age": user.age
        }
        return JsonResponse(req_dict)