from django.db import models

class BoardList(models.Model):
    board_name = models.CharField(max_length=20, null=False)
    user_name = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=100, null=False)
    test = models.CharField(max_length=10)
