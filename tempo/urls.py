
from django.urls import path
from . import views

urlpatterns = [
    path('', views.timer_home, name='timer_home'),
    path('start_timer/', views.start_timer, name='start_timer'),
    path('stop_timer/', views.stop_timer, name='stop_timer'),
    path('reset_timer/', views.reset_timer, name='reset_timer'),
    path('timer_view/', views.timer_view, name='timer_view'),
    path('cronometro_view/', views.cronometro_view, name='cronometro_view'),
]
