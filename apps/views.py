from http import HTTPStatus

from django.contrib.auth.decorators import login_required
from django.db.models import Sum, F, Q
from django.http import JsonResponse
from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated

from apps.models import IncomeExpenses


# Create your views here.

@extend_schema(tags=['expenses'])
@api_view(['GET'])
def expenses_about_api_view(request):
    token = request.headers.get("token")
    user = Token.objects.get(key=token).user
    data = IncomeExpenses.objects.filter(user=user).annotate(
        total_income=Sum('amount' , filter=Q(is_expenses=True)),
        total_expenses=Sum('amount' , filter=Q(is_expenses=False))
    ).annotate(total = F("total_income")-F("total_expenses")).values("total_income" ,"total_expenses" ,"total" )
    return JsonResponse(data[0], status=HTTPStatus.OK)


def is_login(function):
    def wrapper(*args , **kwargs):
        # token = request.headers.get("token")
        # user = Token.objects.get(key=token).user
        print(args)
    return wrapper


@extend_schema(tags=['category'])
@api_view(['GET'])
@is_login
def category_list_api_view(request, user):
    data = IncomeExpenses.objects.filter(user=user).annotate(
        total_income=Sum('amount' , filter=Q(is_expenses=True)),
        total_expenses=Sum('amount' , filter=Q(is_expenses=False))
    ).annotate(total = F("total_income")-F("total_expenses")).values("total_income" ,"total_expenses" ,"total" )
    return JsonResponse(data[0], status=HTTPStatus.OK)



