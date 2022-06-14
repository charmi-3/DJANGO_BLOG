from django import forms
from .models import *
class AddBlog(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','body')
        widget = {
            'title':forms.TextInput(),
            'body':forms.Textarea(),
        }