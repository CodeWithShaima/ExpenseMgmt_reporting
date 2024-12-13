from django.shortcuts import render
import requests
from .models import Expense
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ExpenseSerializer
from django.contrib.auth.decorators import login_required

@login_required
def fetchExpense(request):
   
    expenses = Expense.objects.filter(user=request.user)

    return render(request, 'expense.html', {'expenses': expenses})


class ExpenseCreateView(APIView):
    def post(self, request):
        data = request.data
        user_id = data.get('user_id')

        # Verify user existence in the user_mgmt microservice
        user_mgmt_url = f"http://127.0.0.1:8000/api/verify-user/{user_id}/"
        try:
            response = requests.get(user_mgmt_url)
            if response.status_code == 404:
                return Response({"error": "User does not exist."}, status=404)
            elif response.status_code != 200:
                return Response({"error": "Failed to verify user."}, status=500)
        except requests.RequestException as e:
            return Response({"error": f"Error contacting user management service: {str(e)}"}, status=500)

        # Create the expense
        expense = Expense.objects.create(
            expensename=data['expensename'],
            amount=data['amount'],
            location=data['location'],
            date=data['date'],
            user_id=user_id
        )
        return Response({"message": "Expense created successfully!", "expense_id": expense.expenseid}, status=201)



class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
        queryset = Expense.objects.all()
        serializer_class = ExpenseSerializer