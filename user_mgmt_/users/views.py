from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import get_object_or_404
from .models import User
from .serializers import UserSerializer
from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to Expense Management System!")


class RegisterView(APIView):
    def post(self, request):
        data = request.data
        data['password']= make_password(data['password']) #hashing password
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class LoginView(APIView):
    def post (self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = get_object_or_404(User, username=username)

        if check_password(password, user.password):
            return Response({'message': 'Login Sucessful!'}, status=status.HTTP_200_OK)
        return Response({'message': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    


class UserListView(APIView):
        def get(self, request):
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


