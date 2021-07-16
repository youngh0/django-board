from django import forms

from comment.models import Comments


class CommentCreationForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['body']