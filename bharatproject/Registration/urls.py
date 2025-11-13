from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('event/', views.event_application_view, name='event_application'),
    path('',RedirectView.as_view(pattern_name='event_application')),
    path("api/ministries/", views.ministries, name="ministries"),
    path("api/states/", views.states, name="states"),
    path("api/districts/", views.districts, name="districts"),
]