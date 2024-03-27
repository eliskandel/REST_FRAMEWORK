from rest_framework import serializers
from .models import User
class UserSerializer(serializers.ModelSerializer):
    # user_name=serializers.CharField(max_length=200)
    # first_name=serializers.CharField( max_length=50)
    # last_name=serializers.CharField(max_length=250)
    # age=serializers.IntegerField()
    class Meta:
        model=User
        fields='__all__'