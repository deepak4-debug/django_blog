from .models import Comment
from django import forms


class CommentForm (forms.ModelForm):
    comment = forms.CharField(label='', widget=forms.Textarea(attrs={
        'rows': '5',
        'placeholder': 'Comment.....'
    }))
    class Meta:
        model = Comment
        fields = ['comment']















'''
#This is for form validation using django in_build ModelForm
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body') # by default django will generates all types of field, but we can define explicitly.
        


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
'''