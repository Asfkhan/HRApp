"""
URL configuration for empManage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from empApp.views import employee_list, employee_create, job_role_list, job_role_create, employee_list, employee_create

urlpatterns = [
    path('job-roles/', job_role_list, name='job_role_list'),
    path('job-roles/create/', job_role_create, name='job_role_create'),
    path('', employee_list, name='employee_list'),
    path('employees/create/', employee_create, name='employee_create'),
   
]

