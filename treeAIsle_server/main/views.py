from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
from .serializers import UserSrializer, CreateUserSerializer
from rest_framework import generics
from django.shortcuts import HttpResponse, render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
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
    serializer_class = UserSrializer


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
                return Response(status=status.HTTP_202_ACCEPTED)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def Register(request):
    print(request)
    try:
        data = json.loads(request.body)
        username = data.get('username')
        user = User.objects.get(username=username)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        password = data.get('password')
        email = data.get('email')
        user = User(username=username,password=password,email=email)
        user.save()
        return Response(status=status.HTTP_201_CREATED)
    except:
        print("An error occured")
        return Response(status=status.HTTP_404_NOT_FOUND)
@csrf_exempt
def login(request): # My boye doesn't want to rerurn a thing
    print(f"{request.body}\n\n\n\n\n\n")
    #if request.method == 'GET':
    try:
        print("Getting data")
        data = json.loads(request.body)
        email = data.get('username')
        print(email)
        password = data.get('password')
        print(data)
        # Check if email exists in the database
        print(email)
        print(password)
        user = User.objects.get(email=email)
        # Verify the password
        # hashed_password = hashlib.sha256(password.encode()).hexdigest()
        #if user.password == hashed_password:
        #        return JsonResponse({'message': 'Login successful'})
        #else:
        #    return JsonResponse({'message': 'Invalid credentials'}, status=401)
        if user.password == password:
            return JsonResponse({'message': 'Login successful'})
        else:
            return JsonResponse({'message': 'Invalid credentials'}, status=401)
    except User.DoesNotExist:
        try:
            data = json.loads(request.body)
            email = data.get('username')
            password = data.get('password')
            
            # Check if email exists in the database
            user = User.objects.get(email=email)            
            # Verify the password
            # hashed_password = hashlib.sha256(password.encode()).hexdigest()
            if user.password == password:
                return JsonResponse({'message': 'Login successful'})
            else:
                return JsonResponse({'message': 'Invalid credentials'}, status=401)
        except User.DoesNotExist:
            return JsonResponse({'message': 'User does not exist'}, status=404)
    except Exception as e:
        # Later here should be a wrong password error
        return JsonResponse({'message': 'An error occurred'}, status=500)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)
