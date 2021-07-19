from rest_framework import serializers
from board.models import BoardList

class BoardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardList
        fields = ['board_name', 'user_name', 'description']