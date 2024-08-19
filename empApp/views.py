# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import JobRole, Employee
from .forms import JobRoleForm, EmployeeForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required, permission_required

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

@login_required
@permission_required('empApp.add_employee', raise_exception=True)
def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html', {'form': form})

# @login_required
# @permission_required('empApp.change_employee', raise_exception=True)
# def employee_update(request, pk):
#     # Your existing code
#     ...

# @login_required
# @permission_required('empApp.delete_employee', raise_exception=True)
# def employee_delete(request, pk):
#     # Your existing code
#     ...


@login_required
@permission_required('empApp.view_employee', raise_exception=True)
def employee_list(request):
    employees = Employee.objects.all()
    
    # Search query
    search_query = request.GET.get('search', '')
    if search_query:
        employees = employees.filter(
            Q(first_name__icontains=search_query) | 
            Q(last_name__icontains=search_query) | 
            Q(job_role__name__icontains=search_query)
        )
    
    # Filter by Job Role
    job_role_id = request.GET.get('job_role', '')
    if job_role_id:
        employees = employees.filter(job_role__id=job_role_id)
    
    # Filter by Hiring Date
    hiring_date = request.GET.get('hiring_date', '')
    if hiring_date:
        employees = employees.filter(date_hired=hiring_date)
    
    job_roles = JobRole.objects.all()
    
    return render(request, 'employee_list.html', {
        'employees': employees,
        'job_roles': job_roles,
        'search_query': search_query,
        'selected_job_role': job_role_id,
        'selected_hiring_date': hiring_date,
    })