from django import forms

from .models import Post


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "text", "main_image", "images_set")