from django.urls import path
from .views import Login, api_index, Register, UserView

urlpatterns = [
    path("view_users", UserView.as_view()),
    path("api/", api_index),
    path("", api_index),
    path("login/", Login),
    path("register", Register),
]
