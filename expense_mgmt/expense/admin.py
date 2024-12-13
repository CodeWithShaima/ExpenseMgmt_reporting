from django.contrib import admin
from .models import Expense

# @admin.register(Expense)
# class ExpenseAdmin(admin.ModelAdmin):
#     list_display = ('expensename', 'amount', 'location', 'date', 'user_id')

admin.site.register(Expense)