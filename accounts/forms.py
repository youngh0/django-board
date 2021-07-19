from django import forms

from accounts.models import User
from board.models import BoardList, Content


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','nickname', 'password']

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','password']

