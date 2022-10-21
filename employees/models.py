"""Employee model"""
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from roles.models import Role


class Employee(models.Model):
    """Class for employee model"""

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('Undisclosed', 'Prefer not to say'),
    ]
    employee_id = models.BigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=11, choices=GENDER_CHOICES)
    role = models.ForeignKey(
        Role, on_delete=models.CASCADE, related_name="role"
        )
    pps_number = models.CharField(max_length=9, unique=True)
    phone_number = PhoneNumberField()
    email = models.CharField(max_length=70, unique=True)
    start_date = models.DateField()

    class Meta:
        """Control ordering for employee model"""
        ordering = ["start_date"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
