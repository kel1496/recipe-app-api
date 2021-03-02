from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTest(TestCase):

    def test_create_user_with_email_succesful(self):
        """TEst creating a new user with an email is successful"""
        email = 'test@londonappdev.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """TEst the email for a new user is normalized"""
        email = 'test@LONDONAPPDEV.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test if email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')


    def test_create_new_superuser(self):
        """TEst creating a new superuser"""
        user = get_user_model().objects.create_superuser(
        'test²londonappdev.com',
        'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
