from django.db import models
from django.shortcuts import render
class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15)  
    class Meta:  
        db_table = "employee"  

def employee_list(request):
    employees = Employee.objects.all()  # Fetch all employees from the database
    return render(request, 'your_template_name.html', {'employees': employees})
