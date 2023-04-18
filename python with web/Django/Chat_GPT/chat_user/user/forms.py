from django import forms
from .models import UserProfile

class UserProfileLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        try:
            user_profile = UserProfile.objects.get(username=username)
            if not user_profile.check_password(password):
                raise forms.ValidationError('Incorrect password')
        except UserProfile.DoesNotExist:
            raise forms.ValidationError('Unknown user')

        cleaned_data['user_profile'] = user_profile
        return cleaned_data