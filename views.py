from django.http import render
from django.http import HttpResponse


def page (request,*args, **kwargs):
    return HttpResponse("<h1> Hello World </h1>")



