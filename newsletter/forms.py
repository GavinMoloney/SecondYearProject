from django import forms

class SubscriberForm(forms.Form):
    email = forms.EmailField(label='Please enter your email here',
                             max_length=100,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))