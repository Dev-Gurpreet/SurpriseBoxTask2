from rest_framework.serializers import ModelSerializer
from .models import Users

class UsersSerializer(ModelSerializer):

    class Meta:
        model = Users
        fields = ['id', 'username', 'is_winner']