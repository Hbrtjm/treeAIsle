from django.urls import path
from .views import login,hello

urlpatterns = [
    path('api/login/<str:username>,<str:password>', login, name='login'),
    path('henlo',hello,name="henlo")    
]
