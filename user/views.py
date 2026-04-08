
# Django imports for rendering, HTTP responses, and models
from django.shortcuts import render, HttpResponseRedirect, Http404
from items.models import Category, Product
from user.models import Wishlist, Basket
import math
from django.http import JsonResponse



# Helper class for product info
class item_info:
    def __init__(self, name, category, price, stock, id, cid, quan):
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock
        self.id = id
        self.catId = cid
        self.quantity = quan



# Show user's basket page
def basket(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/account/signin")
    products = Product.objects.filter(basket__user=request.user)
    basket_items = Basket.objects.filter(user=request.user)
    returnList = [
        item_info(
            i.name,
            i.category.name,
            i.price,
            i.stock,
            i.id,
            i.category.id,
            basket_items.get(product=i).quantity,
        )
        for i in products
    ]
    username = request.user.username if request.user.is_authenticated else "Account"
    return render(
        request,
        "basket.html",
        {"data": returnList, "username": username},
    )



# Show user's wishlist page
def wishlist(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/account/signin")
    products = Product.objects.filter(wishlist__user=request.user)
    returnList = [
        item_info(i.name, i.category.name, i.price, i.stock, i.id, i.category.id, None)
        for i in products
    ]
    username = request.user.username if request.user.is_authenticated else "Account"
    return render(
        request,
        "wishlist.html",
        {"data": returnList, "username": username},
    )



# AJAX: get products for a specific page and category
def to_page(request):
    target_page = int(request.GET.get("page", 1))
    target_category = int(request.GET.get("cat", 0))
    if target_category > 0:
        try:
            category = Category.objects.get(id=target_category)
            products = Product.objects.filter(category=category)
        except:
            raise Http404
    else:
        products = Product.objects.all()
    max_page_num = math.ceil(Product.objects.count() / 10)
    if target_page < 1 or target_page > max_page_num:
        return JsonResponse({
            "size": 0,
            "products_names": [],
            "product_categories": [],
            "product_prices": [],
            "product_stocks": [],
            "ids": [],
            "catids": [],
        })
    else:
        names, categories, prices, stocks, ids, cids = [], [], [], [], [], []
        From = (target_page - 1) * 10
        To = From + 10
        products = products[From:To]
        for i in products:
            names.append(i.name)
            categories.append(i.category.name)
            prices.append(i.price)
            stocks.append(i.stock)
            ids.append(i.id)
            cids.append(i.category.id)
        return JsonResponse({
            "size": len(products),
            "products_names": names,
            "product_categories": categories,
            "product_prices": prices,
            "product_stocks": stocks,
            "ids": ids,
            "catids": cids,
        })



# Show item detail page
def to_item(request):
    target_item_id = int(request.GET.get("id", 0))
    if target_item_id > 0:
        try:
            product = Product.objects.get(id=target_item_id)
        except Product.DoesNotExist:
            raise Http404
        username = request.user.username if request.user.is_authenticated else "Account"
        return render(
            request,
            "item_template.html",
            {
                "name": product.name,
                "description": product.description,
                "price": product.price,
                "category": product.category.name,
                "stock": product.stock,
                "username": username,
            },
        )



# Check if item is in stock and add to wishlist (AJAX)
def checkstock(request):
    target_item_id = int(request.GET.get("id", 0))
    if target_item_id > 0:
        try:
            product = Product.objects.get(id=target_item_id)
        except:
            return JsonResponse({"in_stock": False})
    if product.stock > 0:
        Wishlist.objects.get_or_create(user=request.user, product=product)
        return JsonResponse({"in_stock": True})
    else:
        return JsonResponse({"in_stock": False})



# Show products by category (first 10)
def view_by_category(request):
    target_cat_id = int(request.GET.get("id", 0))
    if target_cat_id > 0:
        try:
            category = Category.objects.get(id=target_cat_id)
            products = Product.objects.filter(category=category)[:10]
        except:
            raise Http404
        returnList = [
            item_info(i.name, category.name, i.price, i.stock, i.id, i.category.id, None)
            for i in products
        ]
        username = request.user.username if request.user.is_authenticated else "Account"
        return render(
            request,
            "item_list_template.html",
            {
                "size": products.count(),
                "category": category.name,
                "products": returnList,
                "username": username,
            },
        )



# Remove item from wishlist (AJAX)
def removeItem(request):
    target_item_id = int(request.GET.get("id", 0))
    if target_item_id > 0:
        deleted, _ = Wishlist.objects.filter(
            user=request.user, product_id=target_item_id
        ).delete()
        if deleted:
            return JsonResponse({"removed": True})
        else:
            return JsonResponse({"removed": False})
    else:
        return JsonResponse({"removed": False})


def removeItemFromBakset(request):
    target_item_id = int(request.GET.get("id", 0))
    if target_item_id > 0:
        deleted, _ = Basket.objects.filter(
            user=request.user, product_id=target_item_id
        ).delete()
        if deleted:
            return JsonResponse({"removed": True})
        else:
            return JsonResponse({"removed": False})
    else:
        return JsonResponse({"removed": False})
