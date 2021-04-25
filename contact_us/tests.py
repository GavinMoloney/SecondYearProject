from django.test import TestCase
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError
from .forms import ContactForm
from accounts.models import CustomUser
from http import HTTPStatus
from django.core.exceptions import ValidationError
from django.core import mail
from django.urls import reverse

class ContactTest(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='X00166625@mytudublin.ie',
            password='Ruffian23')

    def tearDown(self):
        self.user.delete()
        
    def test_contact_form(self):
        form = ContactForm(data={'your_email': 'moloney,gavingmail.com', 'subject':'subject', 'message':'message'})
        self.assertEqual(form.errors['your_email'], ['Enter a valid email address.'])

    def test_contact_form_missing_field(self):
        form = ContactForm(data={'your_email': 'moloney,gavingmail.com', 'subject':'', 'message':'message'})
        self.assertEqual(form.errors['your_email'], ['Enter a valid email address.'])
        self.assertFalse(form.is_valid()) 
        self.assertTrue(form.errors)
