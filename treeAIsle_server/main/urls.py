from django.urls import path
from .views import Login,login, api_index, UserView, Register

urlpatterns = [
    path('view_users',UserView.as_view()),
    path('api/',api_index),
    path('',api_index),
    path('api/login', Login), 
    path('api/register',Register),
]
