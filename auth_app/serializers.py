from django.contrib.auth.hashers import make_password, check_password
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer, Serializer

from apps.models import Category
from auth_app.models import User


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "first_name" , "email" , 'password'

    def validate_password(self, value):
        return make_password(value)

class LoginSerializer(Serializer):
    email = CharField(max_length=255)
    password = CharField(max_length=30)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        query = User.objects.filter(email=email)
        if query.exists():
            user = query.first()
            if check_password(password , user.password):
                self.instance = user
            else:
                raise ValidationError("Password xato!")
        else:
            raise ValidationError("Email Topilmadi !")
        return attrs


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "name" ,
