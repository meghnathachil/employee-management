from rest_framework import viewsets
from .models import Department, Employee, Attendance, Performance
from .serializers import DepartmentSerializer, EmployeeSerializer, AttendanceSerializer, PerformanceSerializer
from django.shortcuts import render
from collections import Counter
from datetime import timedelta, date

def charts_view(request):
    # Pie Chart: Employees per Department
    dept_data = Department.objects.all()
    department_labels = [dept.name for dept in dept_data]
    department_counts = [Employee.objects.filter(department=dept).count() for dept in dept_data]

    # Bar Chart: Monthly Attendance Overview
    attendance = Attendance.objects.filter(date__gte=date.today() - timedelta(days=30))
    date_counter = Counter(att.date.strftime('%Y-%m-%d') for att in attendance if att.status == 'Present')
    bar_labels = list(date_counter.keys())
    bar_values = list(date_counter.values())

    print("Department labels:", department_labels)
    print("Counts:", department_counts)
    print("Bar labels:", bar_labels)
    print("Bar values:", bar_values)

    context = {
        'department_labels': department_labels,
        'department_counts': department_counts,
        'bar_labels': bar_labels,
        'bar_values': bar_values,
    }
    return render(request, 'charts.html', context)

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
