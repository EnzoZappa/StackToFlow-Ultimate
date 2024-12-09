from django.urls import path
from .views import whiteboard_view

urlpatterns = [
    path('', whiteboard_view, name='whiteboard'),
]
