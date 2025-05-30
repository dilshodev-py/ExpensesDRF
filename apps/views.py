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
    user = Token.objects.get(key=token)
    data = IncomeExpenses.objects.filter(user=user).annotate(
        total_income=Sum('amount' , filter=Q(is_expenses=False)),
        total_expenses=Sum('amount' , filter=Q(is_expenses=True))
    ).annotate(total = F("total_income")-F("total_expenses")).values_list("total_income" ,"total_expenses" ,"total" )
    print(data)

