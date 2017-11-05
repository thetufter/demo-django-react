from django import forms
from .models import Person


class ContactForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'email')
