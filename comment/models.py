from django.db import models


# Create your models here.
from board.models import BoardContent


class Comments(models.Model):
    content = models.ForeignKey(BoardContent, on_delete=models.CASCADE)
    body = models.CharField(max_length=300, null=False)
    author = models.CharField(max_length=20, null=False)
    date = models.DateField(auto_now_add=True)
