from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Category, Product
from user.models import Basket


class AddBasketTest(TestCase):
    def setUp(self):
        # Create a test category
        self.category = Category.objects.create(name="Test")
        # Create a test product
        self.product = Product.objects.create(
            name="Test Object",
            description="It's a test item.",
            price=Decimal("2.50"),
            category=self.category,
            stock=5,
        )
        # Create a test user
        User = get_user_model()
        self.user = User.objects.create_user(
            username="kevin",
            password="testpass123",
        )

    def test_addbasket_increases_quantity_when_same_product_added_twice(self):
        """
        Test that adding the same product to the basket twice increases its quantity to 2.
        """
        # Log in as the test user
        self.client.login(username="kevin", password="testpass123")
        # Add the product to the basket twice
        self.client.get(reverse("add_basket"), {"id": self.product.id})
        self.client.get(reverse("add_basket"), {"id": self.product.id})
        # Retrieve the basket item and check the quantity
        basket_item = Basket.objects.get(user=self.user, product=self.product)
        self.assertEqual(basket_item.quantity, 2)