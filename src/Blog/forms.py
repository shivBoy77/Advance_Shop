from django import forms
from .models import NewsLetterUser


class NewsLetterSignupForm(forms.ModelForm):
    class Meta:
        model = NewsLetterUser
        fields = ['email']

        def clean_email(self):
            email = self.cleaned_data.get('email')
            return email
