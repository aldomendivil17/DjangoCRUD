from django import forms
from django.contrib.auth.models import User

class UpdateUsernameForm(forms.ModelForm):
    username = forms.CharField(max_length=150, help_text='')

    class Meta:
        model = User
        fields = ['username']