from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
from .serializers import UserSrializer
from rest_framework import generics
from django.shortcuts import HttpResponse, render
import hashlib
import json


class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSrializer


def api_index(request, *args, **kwargs):
    return render(request,'api_index.html')

@csrf_exempt
def login(request):
    print(f"{request}\n\n\n\n\n\n")
    #if request.method == 'GET':
    try:
        data = json.loads(request.headers)
        email = data.get('username')
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
            data = json.loads(request.headers)
            email = data.get('username')
            password = data.get('password')
            
            # Check if email exists in the database
            user = User.objects.get(username=username)            
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
