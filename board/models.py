from django.db import models
from django.db.models import CASCADE


class BoardList(models.Model):
    board_name = models.CharField(max_length=20, null=False)
    user_name = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=100, null=False)
    test = models.CharField(max_length=10)

    # def __str__(self):
        # return self.id

class BoardContent(models.Model):
    board_id = models.ForeignKey(BoardList, on_delete=models.CASCADE, related_name='board_content')
    title = models.CharField(max_length=20, null=False)
    content = models.CharField(max_length=300, null=False)
    author = models.CharField(max_length=20, null=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    # views추가 예정
