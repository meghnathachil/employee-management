from django.urls import path, include
from .views import charts_view
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, EmployeeViewSet, AttendanceViewSet, PerformanceViewSet

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'performance', PerformanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('charts/', charts_view),
]
