from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def _faculty_name(request):
    name = (request.user.first_name or request.user.username or "Faculty")
    if "@" in name:
        name = name.split("@")[0]
    return name.strip().title()


@login_required
def dashboard(request):
    return render(request, "faculty/dashboard.html", {"display_name": _faculty_name(request)})


@login_required
def my_courses(request):
    return render(request, "faculty/my_courses.html", {"display_name": _faculty_name(request)})


@login_required
def live_class(request):
    return render(request, "faculty/live_class.html", {"display_name": _faculty_name(request)})


@login_required
def my_notes(request):
    return render(request, "faculty/my_notes.html", {"display_name": _faculty_name(request)})


@login_required
def quiz_exams(request):
    return render(request, "faculty/quiz_exams.html", {"display_name": _faculty_name(request)})


@login_required
def assignments(request):
    return render(request, "faculty/assignments.html", {"display_name": _faculty_name(request)})


@login_required
def study_material(request):
    return render(request, "faculty/study_material.html", {"display_name": _faculty_name(request)})


@login_required
def announcement(request):
    return render(request, "faculty/announcement.html", {"display_name": _faculty_name(request)})


@login_required
def students(request):
    return render(request, "faculty/students.html", {"display_name": _faculty_name(request)})


@login_required
def enquiry(request):
    return render(request, "faculty/enquiry.html", {"display_name": _faculty_name(request)})


@login_required
def profile(request):
    return render(request, "faculty/profile.html", {"display_name": _faculty_name(request)})

