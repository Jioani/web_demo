from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def first_view_func(request):
    return HttpResponse('<h1>hello world</h1>')
