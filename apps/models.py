
from django.db import models
from django.db.models import Model, ForeignKey, CASCADE
from django.db.models.fields import CharField, BooleanField, DecimalField, TextField


# Create your models here.

class Category(Model):
    name = CharField(max_length=255)
    is_expenses = BooleanField()

class IncomeExpenses(Model):
    amount = DecimalField(max_digits=9 , decimal_places=0)
    description = TextField()
    category = ForeignKey('apps.Category' , CASCADE , related_name="incomeExpenses_list")
    user = ForeignKey('auth_app.User' , CASCADE , related_name='incomeExpenses_list')
    is_expenses = BooleanField()

