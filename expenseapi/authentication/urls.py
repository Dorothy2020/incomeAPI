from django.urls import path
from .views import RegisterView, VerifyEmail
from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg.views import openapi

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify")
]
