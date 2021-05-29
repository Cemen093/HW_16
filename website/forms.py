from django import forms

from website.models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = 'created_at', 'updated_at', 'author'
