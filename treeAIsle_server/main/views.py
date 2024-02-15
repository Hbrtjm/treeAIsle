from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
from .serializers import UserSerializer, CreateUserSerializer
from rest_framework import generics
from django.shortcuts import HttpResponse, render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .validators import is_valid_password, validate_email
import hashlib
import json

class CreateUserSerializer(APIView):
    serializer_class = CreateUserSerializer
    def post(self,request,format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.data.email
            username = serializer.data.username
            password = serializer.data.password
            host=''
            queryset = User.objects.filter(host=host)
            if queryset.exists():
                user = queryset[0] 
                user.username = username
                user.email = user.email
                user.password = user.password
        else:
            user = User()



class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def api_index(request, *args, **kwargs):
    return render(request,'api_index.html')

def new_login():
    pass

def LoginView():
    pass

@api_view(['POST'])
def Login(request):
    print(request)
    try:
        data = json.loads(request.body)
        email = data.get('username')
        password = data.get('password')
        user = User.objects.get(email=email)
        if user.password == password:
            return Response(status=status.HTTP_202_ACCEPTED)
    except User.DoesNotExist:
        try:
            username = data.get('username')
            user = User.objects.get(username=username)
            if user.password == password:
                serializer = UserSerializer(user)
                return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        except User.DoesNotExist:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    return Response(status=status.HTTP_401_UNAUTHORIZED)
@api_view(['POST'])
def Register(request):
    print(request)
    try:
        
        data = json.loads(request.body)
        username = data.get('username')
        user = User.objects.get(username=username)
        return Response(status=status.HTTP_409_CONFLICT)
    except User.DoesNotExist:
        try:
            email=data.get('email')
            user = User.objects.get(email=email)
            return Response(status=status.HTTP_409_CONFLICT)
        except User.DoesNotExist:
            error_flag = False
            password = data.get('password')
            email = data.get('email')
            if not validate_email(email):
                
                # Here it should be pointed out that email was wrong
                error_flag = True
                print("Wrong email")
                
            elif len(username) < 4 or len(username) > 100 or username=='':
                
                # Here we put into JSON what's wrong with the username
                error_flag = True
                print("Wrong username")
            elif len(password) < 8 or is_valid_password():
                error_flag = True
            
            if error_flag:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
            user = User(username=username,password=password,email=email)
            user.save()
            return Response(status=status.HTTP_201_CREATED)
        except:
            print("An error occured")
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

