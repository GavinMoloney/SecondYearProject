from django.test import TestCase
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError
from .forms import SubscriberForm
from accounts.models import CustomUser
from .models import Subscriber
from http import HTTPStatus
from django.core.exceptions import ValidationError
from django.core import mail
from django.urls import reverse

class NewsletterTest(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='X00166625@mytudublin.ie',
            password='Ruffian23')

    def tearDown(self):
        self.user.delete()
        
    def test_newsletter(self):
        form = SubscriberForm(data={'email': 'moloney,gavingmail.com'})
        self.assertEqual(form.errors['email'], ['Enter a valid email address.'])

