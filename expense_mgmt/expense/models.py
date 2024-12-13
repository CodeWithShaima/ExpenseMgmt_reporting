
from django.db import models


class Expense(models.Model):
    expenseid=models.AutoField(primary_key=True)
    expensename=models.CharField(max_length=100)
    amount=models.DecimalField(max_digits=10, decimal_places=2)
    location=models.CharField(max_length=200)
    date=models.DateField()
    user_id = models.IntegerField()
    
    def __str__(self):
        return self.expensename