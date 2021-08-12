# cash_user/serializers.py
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'password'
        )
        # extra_kwargs = {'password': {'write_only': True}}
        # read_only_fields = ('token',)
