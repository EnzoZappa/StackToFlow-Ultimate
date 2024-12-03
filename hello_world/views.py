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


def home(request):
    return render(request, "hello_world\\templates\\home.html")