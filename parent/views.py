from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def _parent_name(request) -> str:
    name = (request.user.first_name or request.user.username or "Parent")
    if "@" in name:
        name = name.split("@")[0]
    return name.strip().title()


@login_required
def dashboard(request):
    return render(request, "parent/dashboard.html", {"display_name": _parent_name(request)})


@login_required
def student_overview(request):
    return render(request, "parent/student_overview.html", {"display_name": _parent_name(request)})


@login_required
def attendance_monitoring(request):
    return render(request, "parent/attendance_monitoring.html", {"display_name": _parent_name(request)})


@login_required
def performance_reports(request):
    return render(request, "parent/performance_reports.html", {"display_name": _parent_name(request)})


@login_required
def fees_payments(request):
    return render(request, "parent/fees_payments.html", {"display_name": _parent_name(request)})


@login_required
def exam_results(request):
    return render(request, "parent/exam_results.html", {"display_name": _parent_name(request)})


@login_required
def announcement(request):
    return render(request, "parent/announcement.html", {"display_name": _parent_name(request)})


@login_required
def enquiry(request):
    return render(request, "parent/enquiry.html", {"display_name": _parent_name(request)})


@login_required
def settings(request):
    return render(request, "parent/settings.html", {"display_name": _parent_name(request)})
