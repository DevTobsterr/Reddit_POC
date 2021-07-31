from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def application_home(request):
    return HttpResponse("<a> WELCOME </a>")