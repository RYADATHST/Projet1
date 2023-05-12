from django import forms
from django.forms.widgets import TextInput

class ContactUsForm(forms.Form):
    nom=forms.CharField(required=False,max_length=1000, widget=forms.TextInput(attrs={'size': '50','placeholder': 'Entrez un nom de domaine...'}))
