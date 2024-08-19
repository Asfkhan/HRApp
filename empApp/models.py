from django.db import models
from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType


# Create your models here.
class JobRole(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    job_role = models.ForeignKey(JobRole, on_delete=models.CASCADE)
    date_hired = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.job_role.name}"
    

@receiver(post_migrate)
def create_user_groups(sender, **kwargs):
    # Create Hiring Manager group if it doesn't exist
    hiring_manager_group, created = Group.objects.get_or_create(name='Hiring Manager')

    # Get or create permissions for Employee model
    content_type = ContentType.objects.get_for_model(Employee)
    can_add_employee = Permission.objects.get(codename='add_employee', content_type=content_type)
    can_change_employee = Permission.objects.get(codename='change_employee', content_type=content_type)
    can_delete_employee = Permission.objects.get(codename='delete_employee', content_type=content_type)

    # Assign permissions to the Hiring Manager group
    hiring_manager_group.permissions.add(can_add_employee, can_change_employee, can_delete_employee)