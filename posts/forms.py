from django import forms
from .models import Image, Profile

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile', 'date_posted']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['owner']        