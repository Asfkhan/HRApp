# urls.py
from django.urls import path
from .views import job_role_list, job_role_create, employee_list, employee_create

urlpatterns = [
    path('job-roles/', job_role_list, name='job_role_list'),
    path('job-roles/create/', job_role_create, name='job_role_create'),
    path('', employee_list, name='employee_list'),
    path('employees/create/', employee_create, name='employee_create'),
]
