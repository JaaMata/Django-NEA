from django import forms
from django.core.exceptions import ValidationError
from django.db import models
from django.forms import ModelForm
from .models import Student





class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'date_of_birth',
                  'home_address', 'home_phone_number', 'gender', 'tutor_group')


class StudentSearchForm(forms.Form):
    student_id = forms.CharField(max_length=13, required=True)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=200, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)


class UserCreationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(), required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter you password'}), required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Renter you password'}), required=True)
    first_name = forms.CharField(widget=forms.TextInput(), required=True)
    last_name = forms.CharField(widget=forms.TextInput(), required=True)

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if not len(password1) >= 8:
            raise forms.ValidationError('The password entred is less then 8 characters.')
        if not password1 == password2:
            raise forms.ValidationError("The passwords entered don't match.")
        return True



