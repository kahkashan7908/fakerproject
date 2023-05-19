from django.db import models
#creating table
class employeeData(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    salary=models.IntegerField()
    company=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=100)
    address=models.CharField(max_length=100)