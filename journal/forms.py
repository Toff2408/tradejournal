from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import *


class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    password1 = forms.CharField(max_length=50)
    password2 = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

    # LONG_SHORT_CHOICES = [
    #     ('TRUE', 'Long'),
    #     ('FALSE', 'Short'),
    # ]

    # longorshort = forms.ChoiceField(
    #     choices=LONG_SHORT_CHOICES,
    #     widget=forms.Select
    # )

class JournalForm(forms.ModelForm):
        class Meta:
            model = Journal
            fields = [
                'date', 'pair', 'time_open', 'time_close', 'duration', 'session', 
                'longorshort', 'entry', 'stop_loss', 'outcome', 'rr', 'note'
            ]
