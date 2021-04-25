from django.test import TestCase
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError
from accounts.models import CustomUser
from http import HTTPStatus
from django.core.exceptions import ValidationError
from django.core import mail
from django.urls import reverse

class OrderTest(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='X00166625@mytudublin.ie',
            password='Ruffian23')

    def tearDown(self):
        self.user.delete()
        



