from django import forms
from firstaid_app.models  import Library, User, Disease
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):

    password = forms.CharField(widget= forms.PasswordInput())
    
    class Meta():
        model = User
        fields = ('username','email','password')

        widgets = {

        }

class LibraryForm(forms.ModelForm):

    class Meta():
        model = Library
        fields = ('name',)

        widgets = {

        }

class DiseaseForm(forms.ModelForm):

    class Meta():
        model = Disease
        fields = ('name','about','symptoms','causes','treatment')

        widgets = {

        }

