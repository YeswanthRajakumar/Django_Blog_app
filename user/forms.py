from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile


class Custom_User_Form(UserCreationForm):
    email = forms.EmailField(required=False)
    contact = forms.CharField(max_length=10, min_length=10, required=False)

    # Meta is used to specify the model which the form is interacting

    class Meta:
        model = User
        # names in HTML tags
        fields = ['username', 'contact', 'email', 'password1', 'password2']


class User_Update_Form(forms.ModelForm):
    email = forms.EmailField(required=False)
    contact = forms.CharField(max_length=10, min_length=10, required=False)

    # Meta is used to specify the model which the form is interacting

    class Meta:
        model = User
        # names in HTML tags
        fields = ['username', 'contact', 'email']


class Profile_Update_Form(forms.ModelForm):
    # Meta is used to specify the model which the form is interacting

    class Meta:
        model = Profile
        # names in HTML tags
        fields = ['profile_pic']
