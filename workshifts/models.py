"""Workshift model"""
from django.db import models
from roles.models import Role
from employees.models import Employee
# Create your models here.


class Workshift(models.Model):
    """Class for workshift model"""

    workshift_id = models.BigAutoField(primary_key=True)
    employee_id = models.ForeignKey(
        Employee, on_delete=models.CASCADE,
        related_name="employee_id_workshift_set"
    )
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    role_id = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        related_name="role_id_workshift_set"
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Control ordering for workshift model"""

        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.employee_id}: {self.start_time} - {self.end_time}"
