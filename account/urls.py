from django.urls import path
from . import views

urlpatterns = [
    # path("signin/", views.signin),
    path("signup/", views.register),
    path("logout/", views.log_out),
    path("signin/", views.sign_in),
]
