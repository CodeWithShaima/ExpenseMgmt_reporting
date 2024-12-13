from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django.http import JsonResponse




class VerifyUserView(APIView):
    def get(self, request, user_id):
        try:
        
            user = User.objects.get(id = user_id)
            return JsonResponse({"user": {"id": user.id, "username": user.username}})
        except User.DoesNotExist:
             return JsonResponse({"error": "User does not exist."}, status=404)
            

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



class UpdateUserView(APIView):
    def put(self, request, user_id):
        # Fetch user based on the ID
        user = get_object_or_404(User, id=user_id)

        # Use the serializer to validate and update user data
        serializer = UserSerializer(user, data=request.data, partial=True)  # partial=True allows partial updates
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class DeleteUserView(APIView):
    def delete(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        user.delete()
        return Response({"message": "User deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)    