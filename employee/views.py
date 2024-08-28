from django.shortcuts import render, redirect  
from employee.forms import EmployeeForm  
from employee.models import Employee 
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
# Create your views here.  
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/show')  # Redirect to /show after login
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, 'employee/login.html')

def logout_view(request):
    logout(request)
    return redirect('/login')


def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})  

@login_required(login_url='/login/')
def show(request):  
    employees = Employee.objects.all()  
    return render(request,"show.html",{'employees':employees})

@login_required(login_url='/login/')
def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  

@login_required(login_url='/login/')
def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})  

@login_required(login_url='/login/')
def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")  
