from django.urls import path
from .views import Login, api_index, UserView, Register
'''
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
'''

urlpatterns = [
    path('view_users',UserView.as_view()),
    path('api/',api_index),
    path('',api_index),
    path('api/login', Login), 
    path('api/register',Register),
]
