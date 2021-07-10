from django import forms

from board.models import BoardList


class BoardCreationForm(forms.ModelForm):
    class Meta:
        model = BoardList
        fields = ['board_name','description']
        labels = {
            'board_name' : '게시판 이름',
            'description' : '게시판 설명'
        }
        widgets = {
            'board_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'description' : forms.Textarea(attrs={'class': 'form-control', 'rows': 10})
        }