from django import forms
from .models import Employee, Training, Enrollment


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'department']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Email'
            }),
            'department': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Department'
            }),
        }


class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = ['title', 'description', 'duration']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Training Title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4
            }),
            'duration': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Duration in Hours'
            }),
        }


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = [
            'employee',
            'training',
            'status',
            'completed_date'
        ]

        widgets = {
            'employee': forms.Select(attrs={
                'class': 'form-control'
            }),
            'training': forms.Select(attrs={
                'class': 'form-control'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            }),
            'completed_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }