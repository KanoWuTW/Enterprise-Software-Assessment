from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="product_list"),
    path("main-to/", views.to_page, name="change_page"),
    path("item/", views.to_item, name="view_item"),
    path("item/search/", views.search, name="search_item"),
    path("item/addwishlist/", views.addwishlist, name="addwish_list"),
    path("item/addbasket/", views.addbasket, name="add_basket"),
    path("cat/", views.view_by_category, name="view_items_by_cat"),
]
