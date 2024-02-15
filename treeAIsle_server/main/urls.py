from django.urls import path
from .views import Login,login, api_index, UserView, Register
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('view_users',UserView.as_view()),
    path('api/',api_index),
    path('',api_index),
    path('api/login', Login), 
    path('api/register',Register),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
