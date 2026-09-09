from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Training(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    training = models.ForeignKey(Training, on_delete=models.CASCADE)

    STATUS = [
        ('Enrolled', 'Enrolled'),
        ('Completed', 'Completed'),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default='Enrolled'
    )

    # Completion Date
    completed_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.employee.name} - {self.training.title}"