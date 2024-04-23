from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.shortcuts import render,redirect
from .models import *
from 
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as mymodule_login
from django.contrib.auth.decorators import login_required


# Create your views here.
def login(request):
     if request.method == "POST":
          email = request.POST.get("User-Email")
          password = request.POST.get("User-Password")
          user = authenticate(request, email=email, password=password)
          if user is not None:
               mymodule_login(request, user)
               return redirect('dashboard')
          else:
               messages.error(request, "Email or Password are incorrect!")
               return redirect('login')
     return render(request, 'myapp/login.html')

def signup(request):
     if request.method == "POST":
          name = request.POST.get("first-name")
          email = request.POST.get("User-Email")
          contact = request.POST.get("contact-no")
          password = request.POST.get("User-Password")
          confirm_password = request.POST.get("Confirm-Password")

          if password != confirm_password:
               messages.error(request, 'Passwords do not match.')
               return redirect('signup')

          if signupmodel.objects.filter(email=email).exists() or signupmodel.objects.filter(contact=contact).exists():
               messages.error(request, 'User with this email or contact already exists!')
               return redirect('signup')

          hashed_password = make_password(password)
          new_user = signupmodel(first_name=name, email=email, contact=contact, password=hashed_password)
          new_user.save()

          messages.success(request, 'Account created successfully!')
          return redirect('login')  
     return render(request, 'myapp/sign-up.html')

def dashboard(request):
    if request.user.is_authenticated:
        user_data = signupmodel.objects.get(email=request.user.email)
        name = user_data.name 
        return render(request, 'myapp/dashboard.html', {'name': name})

def logout(request):
    return render(request, 'myapp/logout.html')

def myAttendance(request):
    return render(request, 'myapp/myAttendance.html')

def editprofile(request):
    return render(request, 'myapp/editprofile.html')

def colleagues(request):
    return render(request, 'myapp/colleagues.html')

def employeeList(request):
    return render(request, 'myapp/employeeList.html')

def requestedLeave(request):
    return render(request, 'myapp/requestedLeave.html')

def statusofLeave(request):
    return render(request, 'myapp/statusofLeave.html')

def leaveDetails(request):
    return render(request, 'myapp/leaveDetails.html')

def leaveApplication(request):
    return render(request, 'myapp/leaveApplication.html')

def employeesLeave(request):
    return render(request, 'myapp/employeesLeave.html')

def employeeDetails(request):
    return render(request, 'myapp/employeeDetails.html')

def employeeAttendance(request):
    return render(request, 'myapp/employeeAttendance.html')

def editEmployeesProfile(request):
    return render(request, 'myapp/editEmployeesProfile.html')

def addEmployee(request):
    return render(request, 'myapp/addEmployee.html')
