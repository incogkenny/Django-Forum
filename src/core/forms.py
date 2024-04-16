from django import forms
from .models import User
from django.contrib.auth.password_validation import MinimumLengthValidator, CommonPasswordValidator, NumericPasswordValidator


validators = [MinimumLengthValidator]

class RegisterForm(forms.ModelForm):
    # Outlines specific field attributes like max length.
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    password = forms.CharField(widget=forms.PasswordInput(), validators= validators)
    email = forms.EmailField()



    class Meta:
        model = User # Links User model to this form in database
        #Creates array for fields to be stored in database
        fields = ['username', 'first_name', 'last_name','email', 'password' ]

        def __init__(self, *args, **kwargs):
            super(RegisterForm, self).__init__(*args, **kwargs)
            self.fields['first_name'].widget.attrs.update({'class': 'form-control'}) # adds CSS classes to fields



class LoginForm(forms.ModelForm):
    # Outlines specific field attributes like a password function that asks for certain characters/symbols in the form.
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User # Links User model to this form in database
        # Creates array for fields to be stored in database
        fields = ['email','password']