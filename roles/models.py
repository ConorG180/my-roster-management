from django.db import models


# Create your models here.
class Role(models.Model):
    role_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    hourly_wage = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.title}"
