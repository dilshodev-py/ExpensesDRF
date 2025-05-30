from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer

from auth_app.models import User


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "first_name" , "email" , 'password'

    def validate_password(self, value):
        return make_password(value)
