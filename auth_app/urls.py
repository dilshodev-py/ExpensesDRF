
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

from auth_app.views import register_api_view, login_api_view

urlpatterns = [
       path('register', register_api_view),
       path('login', login_api_view),
]
