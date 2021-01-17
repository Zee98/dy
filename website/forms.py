from django import forms
from website.models import Sms


class SMS(forms.ModelForm):
    class Meta:
        model: Sms
        fields = ('name', 'email', 'message')