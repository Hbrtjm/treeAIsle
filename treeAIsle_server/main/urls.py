from django.urls import path
from .views import login, api_index, UserView

urlpatterns = [
    path('view_users',UserView.as_view()),
    path('api/',api_index),
    path('',api_index),
    path('api/login', login), 
]
