from django.contrib.auth.models import User
from django.test import TestCase

from user.models import Profile


class RegisterTest(TestCase):
    def test_register_creates_user_profile_and_logs_user_in(self):
        """
        Test that user registration creates a user, profile, and logs the user in.
        """
        # Simulate user registration via POST
        response = self.client.post("/account/signup/", {
            "username": "testname",
            "email": "test@example.com",
            "password1": "Apassword12345",
            "password2": "Apassword12345",
            "first_name": "Te",
            "last_name": "St",
            "phone_number": "0912345678",
        })
        # Check for redirect to home page after registration
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/")
        # Check that the user was created
        user = User.objects.get(username="testname")
        self.assertEqual(user.email, "test@example.com")
        # Check that the profile was created with correct info
        profile = Profile.objects.get(user=user)
        self.assertEqual(profile.first_name, "Te")
        self.assertEqual(profile.last_name, "St")
        self.assertEqual(profile.phone_number, "0912345678")
        # Check that the user is logged in after registration
        response = self.client.get("/")
        self.assertTrue(response.wsgi_request.user.is_authenticated)