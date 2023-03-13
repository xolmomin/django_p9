from django import forms
from django.core.exceptions import ValidationError

from apps.models import Contact


# form, modelform

class ContactForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(max_length=255, required=True)
    confirm_password = forms.CharField(max_length=255, required=True)
    address = forms.CharField(max_length=255, required=True)

    def clean_email(self):
        value = self.cleaned_data.get('email')
        if len(value) <= 5:
            raise ValidationError('Please enter valid email address!')
        return value

    def clean_address(self):
        value = self.cleaned_data.get('address')
        if value != 'Toshkent':
            raise ValidationError('Please enter Tashkent')
        return value

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.pop('confirm_password')
        if confirm_password != password:
            raise ValidationError("Password didn't match!")
        return cleaned_data

    class Meta:
        model = Contact
        fields = ('email', 'password', 'address')
