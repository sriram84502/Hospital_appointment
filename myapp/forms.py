from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Patient
from django.contrib import messages
class PatientForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "id":"username",
        "type":"text",
        "name":"username",
        "placeholder":"Enter username"
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        "id":"phone",
        "name":"phone",
        "type":"text",
        "placeholder":"Enter Phone number"
    }))
    name = forms.CharField(widget=forms.TextInput(attrs={
        "id":"name",
        "name":"name",
        "type":"text",
        "placeholder":"Enter your full name"
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        "id":"pass",
        "type":"password",
        "placeholder":"Enter password"

    }))
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        "id":"pass1",
        "type":"password",
        "placeholder":"Confirm Password"
    }))
    city = forms.CharField(widget=forms.TextInput(attrs={
        "id":"city",
        "name":"city",
        "type":"text",
        "placeholder":"Enter Your city"
    }))
    age = forms.CharField(widget=forms.TextInput(attrs={
        "id":"age",
        "name":"age",
        "type":"text",
        "placeholder":"Enter Your age"
    }))
    class Meta:
        model = Patient
        fields = ['name','phone','is_phone_verified','username','city']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['password2']

    def clean_password(self):
        password= self.cleaned_data['password']

        if len(password) < 8:
            raise forms.ValidationError("Your password should be at least 8 Characters")

        return password
        
        