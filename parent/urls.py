from django.urls import path
from . import views

app_name = "parent_app"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("student-overview/", views.student_overview, name="student_overview"),
    path("attendance-monitoring/", views.attendance_monitoring, name="attendance_monitoring"),
    path("performance-reports/", views.performance_reports, name="performance_reports"),
    path("fees-payments/", views.fees_payments, name="fees_payments"),
    path("exam-results/", views.exam_results, name="exam_results"),
    path("announcement/", views.announcement, name="announcement"),
    path("enquiry/", views.enquiry, name="enquiry"),
    path("settings/", views.settings, name="settings"),
]
