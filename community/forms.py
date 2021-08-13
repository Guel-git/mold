from django import forms
from django import forms
from .models import *

class CommentForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('created_by', 'messages')