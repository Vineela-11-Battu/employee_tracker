from django.contrib import admin
from .models import Employee, Training, Enrollment

admin.site.register(Employee)
admin.site.register(Training)
admin.site.register(Enrollment)
