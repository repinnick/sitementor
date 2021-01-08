from django import forms
from django.contrib.auth.forms import AuthenticationForm


class SearchForm():
    pass


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='User Name', max_length=100)
    password = forms.CharField(label='Password')


class RegistrationForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    user_name = forms.CharField(label='User Name', max_length=100)
    email = forms.EmailField(label='E-mail')
    types = forms.CharField(label='Type')
    password = forms.CharField()
    password_retype = forms.CharField()


class SiteProfileForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    phone_number = forms.CharField(max_length=12)
    about_you = forms.Textarea()
    # language_list = forms.ChoiceField()
    user_photo = forms.ImageField()
    linked_in = forms.CharField(max_length=250)

