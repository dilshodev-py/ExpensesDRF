from http import HTTPStatus

from django.http import JsonResponse
from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response

from auth_app.serializers import UserModelSerializer


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
@extend_schema(tags=['auth'])
@api_view(['POST'])
def login_api_view(request):
    return JsonResponse({"message": "Login"})
