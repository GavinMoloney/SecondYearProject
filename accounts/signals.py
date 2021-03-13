from django.contrib.auth.signals import signupView, signinView, signoutView
from django.dispatch import receiver

@receiver(signupView)
def log_user_login(sender, request, user, **kwargs):
    print('user logged in')

@receiver(signinView)
def log_user_login_faild(sender, credentials, request, **kwargs):
    print('user faild to log in')

@receiver(signoutView)
def log_user_logout(sender, request, user, **kwargs):
    print('user logged out')