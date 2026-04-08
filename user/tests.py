
# Django test for basket page functionality
from decimal import Decimal
from django.contrib.auth.models import User
from django.test import TestCase
from items.models import Category, Product
from user.models import Basket



class BasketPageTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username="kevin",
            password="testpass123"
        )
        # Create a test category
        self.category = Category.objects.create(name="TestCategory")
        # Create a test product
        self.product = Product.objects.create(
            name="Test Obj",
            description="It's a test object",
            price=Decimal("1010515.23"),
            category=self.category,
            stock=5,
        )
        # Add the product to the user's basket with quantity 2
        Basket.objects.create(
            user=self.user,
            product=self.product,
            quantity=2
        )

    def test_basket_page_shows_user_basket_item(self):
        """
        Test that the basket page displays the correct product and quantity for the logged-in user.
        """
        # Log in as the test user
        self.client.login(username="kevin", password="testpass123")
        # Request the basket page
        response = self.client.get("/user/basket/")
        # Check that the page loads successfully
        self.assertEqual(response.status_code, 200)
        # Check that the product name and quantity appear in the response
        self.assertContains(response, "Test Obj")
        self.assertContains(response, "2")