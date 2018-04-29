from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.views.generic.base import View

from employees.models import Employees, Department
from employees.forms import AddEmployeesForm, ExcludeEmployeeForm, AddDepartment


# Create your views here.
#Redirecting pages from one to another, with arguments

#Index page
def index(request):
    return render(request, 'index.html')


#Showing an specific employee
def show(request, employee_id):
    employee = Employees.objects.get(id=employee_id)
    return render(request, 'employees.html', {"employee" : employee})


#Showing a list of employees
def list(request):
    return render(request, 'list.html', {'employees' : Employees.objects.all()})


#Registering a new employee
def new_employee(request):
    if request.method == "POST":
        form_add = AddEmployeesForm(request.POST)
        if form_add.is_valid():
            form_data = form_add.data

            if Employees.objects.filter(email=form_data['email']).exists():
                form_add.add_error(None, "We already have this e-mail registered")
            else:
                department = Department.objects.get(id=form_data['department'])
                employee = Employees(name=form_data['name'],
                                     email=form_data['email'],
                                     department=department)
                employee.save()
                messages.success(request, 'Employee added successfully!')
                return redirect('/employees/new_employee')
    else:
        form_add = AddEmployeesForm()
    return render(request, 'new_employee.html', {'form_add': form_add})


#Registering a new department
def new_department(request):
    if request.method == "POST":
        form_add_dept = AddDepartment(request.POST)
        if form_add_dept.is_valid():
            form_data = form_add_dept.data

            department = Department(name=form_data['department'])

            department.save()
            messages.success(request, 'Department added successfully!')
            return redirect('/employees/new_department')
    else:
        form_add_dept = AddDepartment()
    return render(request, 'new_department.html', {'form_add_dept': form_add_dept})


#Deleting employee
def delete_employee(request):
    if request.method == "POST":
        form_exclude = ExcludeEmployeeForm(request.POST)
        if form_exclude.is_valid():
            form_data = form_exclude.data
            try:
                deleting = Employees.objects.get(email=form_data['email'])
                deleting.delete()
                messages.success(request, 'Employee excluded successfully!', {'form_exclude': form_exclude})
                return redirect('/employees/delete_employee')
            except ObjectDoesNotExist:
                form_exclude.add_error(None, "We don't have this e-mail registered to be excluded")
                return render(request, 'delete_employee.html', {'form_exclude': form_exclude})
    else:
        form_exclude = ExcludeEmployeeForm()
    return render(request, 'delete_employee.html', {'form_exclude': form_exclude})