from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    #Which models should be used for form
    class Meta:
        model = Post
        fields = ('title', 'text',)
