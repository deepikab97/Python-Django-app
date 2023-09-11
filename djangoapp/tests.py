from django.test import TestCase
from django.db import IntegrityError  # Import IntegrityError
from djangoapp.models import User

class UserModelTestCase(TestCase):
    def setUp(self):
        # Create a User instance for testing
        self.user = User.objects.create(name='John Doe', email='john@example.com')

    def test_user_creation(self):
        # Test that the user was created correctly
        self.assertEqual(self.user.name, 'John Doe')
        self.assertEqual(self.user.email, 'john@example.com')

    def test_user_str_method(self):
        # Test the __str__ method of the User model
        self.assertEqual(str(self.user), 'John Doe')


    def test_user_name_max_length(self):
        # Test the max length of the name field
        max_length = self.user._meta.get_field('name').max_length
        self.assertEqual(max_length, 50)

    def test_user_email_max_length(self):
        # Test the max length of the email field
        max_length = self.user._meta.get_field('email').max_length
        self.assertEqual(max_length, 50)
