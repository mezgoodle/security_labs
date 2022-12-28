from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("logout", views.logout),
    path("register", views.register),
    path("api/public", views.public),
    path("api/private", views.private),
]
