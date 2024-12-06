from django.shortcuts import render, redirect, get_object_or_404  # Rendering templates, redirects, and fetching objects
from django.http import HttpResponse, JsonResponse  # Sending HTTP responses (HTML or JSON)
from django.views import View  # Class-based views
from django.contrib import messages  # Displaying success/error messages
from django.urls import reverse  # Generating URLs by view name
from django.core.paginator import Paginator  # Handling pagination
from django.contrib.auth.decorators import login_required  # Protecting views with login
from django.utils.decorators import method_decorator  # Applying decorators to class-based views
from django.contrib.auth.models import User  # Default user model
from django.db.models import Q  # Complex queries
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm  # Formulários para login e cadastro
from django.contrib.auth import login, authenticate, logout  # Funções para autenticação


def Home(request):
    return render(request, "Main.html", )


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")  # Redireciona para a página inicial após login
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")  # Redireciona para a página inicial após cadastro
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("home")  # Redireciona para a página inicial após logout


def whiteboard_view(request):
    return render(request, "whiteboard.html")

