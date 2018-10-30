# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import (authenticate, get_user_model, login, logout)
from .forms import UserLoginForm


def login_view(request): 
    if request.user.is_authenticated: 
        print "User is already authenticated"
        return redirect("exactly_dashboard_home:index")


    form = UserLoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        login(request, user)

        try:
            next_page = request.GET.get('next')
            return redirect(next_page)
        except:
            return redirect("exactly_dashboard_home:index")

    context = {
        "form": form
    }
    return render(request, "accounts/login.html", context)



def logout_view(request): 
    logout(request)

    context = {
        'logout_message': "You have successfully logged out!",
    }
    return redirect("accounts:login")
    