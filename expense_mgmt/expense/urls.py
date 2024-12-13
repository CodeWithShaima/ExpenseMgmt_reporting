
from expense import views
from django.urls import path
from .views import ExpenseCreateView,ExpenseDetailView

urlpatterns = [
    path('exps/', views.fetchExpense, name='expenses'),
    path('api/create/', ExpenseCreateView.as_view(), name='expense-create'),
    path('api/expenses/<int:pk>/', ExpenseDetailView.as_view(), name='expense-detail'),
]