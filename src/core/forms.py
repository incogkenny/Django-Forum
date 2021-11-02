from django import forms
from .models import User

class RegisterForm(forms.ModelForm):
    # Outlines specific field attributes like max length.
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User # Links User model to this form in database
        #
        fields = ['username', 'first_name', 'last_name','email', 'password' ]

        def __init__(self, *args, **kwargs):
            super(RegisterForm, self).__init__(*args, **kwargs)
            self.fields['first_name'].widget.attrs.update({'class': "form-control rounded-pill border-0 shadow-sm px-4"}) # adds HTML classes to fields

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['email','password']