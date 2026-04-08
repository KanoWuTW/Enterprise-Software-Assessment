from django.urls import path
from . import views

urlpatterns = [
    path("basket/", views.basket),
    path("basket/remove/", views.removeItemFromBakset),
    path("wishlist/", views.wishlist),
    path("wishlist/remove/", views.removeItem),
]
