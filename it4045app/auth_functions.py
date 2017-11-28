__author__ = 'Andrew'
from django.shortcuts import render
from django.contrib.auth import authenticate, login as do_login, logout
def do_auth(request):
    kwargs = {"error": ""}

    user = authenticate(username=request.POST.get("username"), password=request.POST.get("password"))
    print user

    if user:
        do_login(request, user)

    else:
        kwargs['error'] = "Username/Password is invalid"

    return kwargs


def do_logout(request):
    logout(request)
