from django.db import models
from roles.models import Role
from employees.models import Employee
# Create your models here.


class Workshift(models.Model):
    workshift_id = models.BigAutoField(primary_key=True)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="employee_id_workshift_set") 
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="role_id_workshift_set") 
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.employee_id}: {self.start_time} - {self.end_time}"
