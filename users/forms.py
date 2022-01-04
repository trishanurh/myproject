from django import forms
from django.db.models import fields
from django.forms import widgets

from django.contrib.auth.models import User
from .models import Biodata

# ---------------------------------------------------------- FORMS USER ----------------------------------------------------------#

class UserForms(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)
        widgets = {
            "first_name" : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type':'text',
                    'required':True
                }),
            "last_name" : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type':'text',
                    'required':True
                }),
            "email" : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type':'text',
                    'required':True
                }),
        }

# ---------------------------------------------------------- FORMS BIO ----------------------------------------------------------#

class BiodataForms(forms.ModelForm):
    class Meta:
        model = Biodata
        fields = ('alamat', 'telp',)
        widgets = {
            "alamat" : forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'type':'text',
                    'required':True
                }),
            "telp" : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type':'text',
                    'required':True
                }),
        }
