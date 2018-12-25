from django import forms

from mdeditor.fields import MDTextFormField

from .models import Post


class PostForm(forms.ModelForm):

    # text = forms.CharField(widget=MarkdownWidget())
    # text = MarkdownFormField()

    class Meta:
        model = Post
        fields = ('title', 'text',)
