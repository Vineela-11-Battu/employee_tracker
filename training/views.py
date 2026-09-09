from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Employee, Training, Enrollment
from .forms import EmployeeForm, TrainingForm, EnrollmentForm


# ===========================
# Employee Views
# ===========================

def employee_list(request):
    search = request.GET.get('search')

    if search:
        employees = Employee.objects.filter(name__icontains=search)
    else:
        employees = Employee.objects.all()

    return render(request, 'employee_list.html', {
        'employees': employees
    })


def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()

    return render(request, 'add_employee.html', {'form': form})


def edit_employee(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'add_employee.html', {'form': form})


def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    employee.delete()
    return redirect('employee_list')


# ===========================
# Training Views
# ===========================

def training_list(request):
    trainings = Training.objects.all()
    return render(request, 'training_list.html', {'trainings': trainings})


def add_training(request):
    if request.method == 'POST':
        form = TrainingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('training_list')
    else:
        form = TrainingForm()

    return render(request, 'add_training.html', {'form': form})


def edit_training(request, id):
    training = get_object_or_404(Training, id=id)

    if request.method == 'POST':
        form = TrainingForm(request.POST, instance=training)
        if form.is_valid():
            form.save()
            return redirect('training_list')
    else:
        form = TrainingForm(instance=training)

    return render(request, 'add_training.html', {'form': form})


def delete_training(request, id):
    training = get_object_or_404(Training, id=id)
    training.delete()
    return redirect('training_list')


# ===========================
# Enrollment Views
# ===========================

def enrollment_list(request):
    enrollments = Enrollment.objects.all()
    return render(request, 'enrollment_list.html', {'enrollments': enrollments})


def add_enrollment(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enrollment_list')
    else:
        form = EnrollmentForm()

    return render(request, 'add_enrollment.html', {'form': form})


def edit_enrollment(request, id):
    enrollment = get_object_or_404(Enrollment, id=id)

    if request.method == 'POST':
        form = EnrollmentForm(request.POST, instance=enrollment)
        if form.is_valid():
            form.save()
            return redirect('enrollment_list')
    else:
        form = EnrollmentForm(instance=enrollment)

    return render(request, 'add_enrollment.html', {'form': form})


def delete_enrollment(request, id):
    enrollment = get_object_or_404(Enrollment, id=id)
    enrollment.delete()
    return redirect('enrollment_list')


# ===========================
# Dashboard
# ===========================

def dashboard(request):
    total_employees = Employee.objects.count()
    total_trainings = Training.objects.count()
    total_enrollments = Enrollment.objects.count()

    context = {
        'total_employees': total_employees,
        'total_trainings': total_trainings,
        'total_enrollments': total_enrollments,
    }

    return render(request, 'dashboard.html', context)

# ===========================
# Login & Logout
# ===========================

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid Username or Password")

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("login")


def certificate(request, id):
    enrollment = get_object_or_404(Enrollment, id=id)

    return render(request, 'certificate.html', {
        'enrollment': enrollment
    })