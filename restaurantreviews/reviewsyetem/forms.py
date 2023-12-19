from django import forms
from .models import Comment1
from django.forms import ModelForm, Textarea


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment1
        fields = ['title', 'description']
        widgets = {
            'description': Textarea(attrs={'cols': 60, 'rows': 8}),
        }
        
        
class CommentEditForm(forms.ModelForm):
    class Meta:
        model = Comment1
        fields = ['title', 'description']  