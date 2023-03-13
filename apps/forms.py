from django import forms

from apps.models import Contact


# form, modelform

class ContactForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(max_length=255)
    address = forms.CharField(max_length=255)

    class Meta:
        model = Contact
