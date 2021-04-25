from django.test import TestCase
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError
from accounts.models import CustomUser, Profile
from http import HTTPStatus
from django.core.exceptions import ValidationError
from django.core import mail
from django.urls import reverse

class OrderTest(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='Gmoloney',
            email='X00166625@mytudublin.ie',
            password='Ruffian23')

    """
    def test_user_login_correct_credentials(self):
        self.user = authenticate(username='Gmoloney', password='Ruffian23')
        self.assertFalse((self.user is not None) and self.user.is_authenticated)
        login = self.client.login(username='Gmoloney', password='Ruffian23')
        self.assertFalse(login)
        self.assertTrue(self.user.is_active)
        # self.assertFalse(self.user.is_staff)
        # self.assertFalse(self.user.is_superuser)
    """
    """
    def test_user_details(self):
        self.assertEqual(f'{self.user.username}', 'Gmoloney')
        self.assertEqual(f'{self.user.email}', 'X00166625@mytudublin.ie')
        self.assertEqual(f'{self.user.password}', 'Ruffian23')
    """

    def test_user_login_wrong_username(self):
        self.user = authenticate(username='wrong', password='secret')
        self.assertFalse(self.user is not None and self.user.is_authenticated) 

    def test_user_login_wrong_password(self):
        self.user = authenticate(username='testuser', password='wrong')
        self.assertFalse(self.user is not None and self.user.is_authenticated)
    
    def test_login_view(self):
        response = self.client.get(reverse('signin'))
        self.assertEqual(response.status_code, 200)

    def test_create_view(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
