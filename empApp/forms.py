from django import forms
from .models import JobRole, Employee

class JobRoleForm(forms.ModelForm):
    class Meta:
        model = JobRole
        fields = ['name', 'description', 'is_active']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'job_role', 'is_active']
