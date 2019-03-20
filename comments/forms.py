from .models import Comment
from django import forms

class Commetforms(forms.ModelForm):
    # 元类
    class Meta:
        model = Comment
        fields = ["text"]
