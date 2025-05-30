from django.urls import path

from apps.views import expenses_about_api_view

urlpatterns = [
       path("expenses/info" , expenses_about_api_view)
]
