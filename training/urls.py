from django.urls import path
from . import views

urlpatterns = [
    # Employee
    path('', views.employee_list, name='employee_list'),
    path('add/', views.add_employee, name='add_employee'),
    path('edit/<int:id>/', views.edit_employee, name='edit_employee'),
    path('delete/<int:id>/', views.delete_employee, name='delete_employee'),

    # Training
    path('training/', views.training_list, name='training_list'),
    path('training/add/', views.add_training, name='add_training'),
    path('training/edit/<int:id>/', views.edit_training, name='edit_training'),
    path('training/delete/<int:id>/', views.delete_training, name='delete_training'),

    # Enrollment
    path('enrollment/', views.enrollment_list, name='enrollment_list'),
    path('enrollment/add/', views.add_enrollment, name='add_enrollment'),
    path('enrollment/edit/<int:id>/', views.edit_enrollment, name='edit_enrollment'),
    path('enrollment/delete/<int:id>/', views.delete_enrollment, name='delete_enrollment'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # Login & Logout
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),


    path('certificate/<int:id>/', views.certificate, name='certificate'),
]