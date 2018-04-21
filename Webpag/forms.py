from django import forms
from instasafe.models import Post

class UsernameForm(forms.ModelForm):
    post = forms.CharField()

    class Meta:
        model = Post
        fields = ('post',)
