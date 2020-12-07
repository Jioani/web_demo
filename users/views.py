from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from users.models import User


def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        User.objects.create(username=username, password=password)
        return HttpResponse("提交注册请求")
