# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import JobRole, Employee
from .forms import JobRoleForm, EmployeeForm

def job_role_list(request):
    job_roles = JobRole.objects.all()
    return render(request, 'job_role_list.html', {'job_roles': job_roles})

def job_role_create(request):
    if request.method == 'POST':
        form = JobRoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_role_list')
    else:
        form = JobRoleForm()
    return render(request, 'job_role_form.html', {'form': form})

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html', {'form': form})
