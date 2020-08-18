from django import forms
from .models import Image, Profile,Comment

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['author','date_posted', 'likes']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']    

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user','image','date_posted']