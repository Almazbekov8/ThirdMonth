from django.urls import path
from . import views

urlpatterns = [
    path('about-me/', views.about_me_view, name='about_me'),
    path('current-time/', views.current_time_view, name='current_time'),
]
