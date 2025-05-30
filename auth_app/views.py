from http import HTTPStatus

from django.http import JsonResponse
from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response

from auth_app.serializers import UserModelSerializer, LoginSerializer


# Create your views here.



@extend_schema(request=UserModelSerializer , responses=UserModelSerializer)
@extend_schema(tags=['auth'])
@api_view(['POST'])
def register_api_view(request):
    data = request.data
    serializer = UserModelSerializer(data=data)
    if serializer.is_valid():
        obj = serializer.save()
        return JsonResponse(UserModelSerializer(instance=obj).data)
    return Response(serializer.errors , status=HTTPStatus.BAD_REQUEST)



# @extend_schema(request=LoginSerializer)
@extend_schema(tags=['auth'] , request=LoginSerializer)
@api_view(['POST'])
def login_api_view(request):
    data = request.data
    serializer = LoginSerializer(data=data)
    if serializer.is_valid():
        user = serializer.instance
        token = Token.objects.get_or_create(user=user)[0]
        return JsonResponse({"token": token.key})
    else:
        return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)





