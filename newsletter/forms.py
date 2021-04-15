from django import forms

class SubscriberForm(forms.Form):
    email = forms.EmailField(label='Please enter your email below to learn about our latest offers, products and news',
                             max_length=100,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))