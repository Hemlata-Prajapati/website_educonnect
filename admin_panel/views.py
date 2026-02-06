from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render


# -------------------------
# HELPERS
# -------------------------
def _is_admin_user(user) -> bool:
    if not user or not user.is_authenticated:
        return False
    role = getattr(user, "role", "")
    return user.is_superuser or user.is_staff or (str(role).upper() == "ADMIN")


# -------------------------
# AUTH
# -------------------------
def admin_login(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated and _is_admin_user(request.user):
        return redirect("admin_panel:admin_dashboard")

    if request.method == "POST":
        email = (request.POST.get("email") or "").strip()
        password = request.POST.get("password") or ""

        if not email or not password:
            messages.error(request, "Email and password are required.")
            return render(request, "admin_panel/login.html")

        user = authenticate(request, username=email, password=password)

        if user is None:
            try:
                user = authenticate(request, email=email, password=password)
            except TypeError:
                user = None

        if user is None:
            messages.error(request, "Invalid email or password.")
            return render(request, "admin_panel/login.html")

        if not _is_admin_user(user):
            messages.error(request, "You are not authorized to access Admin Panel.")
            return render(request, "admin_panel/login.html")

        login(request, user)
        return redirect("admin_panel:admin_dashboard")

    return render(request, "admin_panel/login.html")


@login_required
def admin_logout(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect("admin_panel:admin_login")


# -------------------------
# DASHBOARD
# -------------------------
@login_required
def admin_dashboard(request: HttpRequest) -> HttpResponse:
    if not _is_admin_user(request.user):
        logout(request)
        return redirect("admin_panel:admin_login")

    display_name = request.user.first_name or request.user.username or "Admin"
    return render(
        request,
        "admin_panel/dashboard.html",
        {"display_name": display_name},
    )


# -------------------------
# USERS
# -------------------------
@login_required
def manage_students(request):
    return render(request, "admin_panel/manage_students.html")


@login_required
def manage_faculty(request):
    return render(request, "admin_panel/manage_faculty.html")


@login_required
def manage_parents(request):
    return render(request, "admin_panel/manage_parents.html")


# -------------------------
# PAYMENTS
# -------------------------
@login_required
def payment_history(request):
    return render(request, "admin_panel/payment_history.html")


@login_required
def fee_packages(request):
    return render(request, "admin_panel/fee_packages.html")


@login_required
def refund_requests(request):
    return render(request, "admin_panel/refund_requests.html")


# -------------------------
# OTHERS
# -------------------------
@login_required
def manage_courses(request):
    return render(request, "admin_panel/manage_courses.html")


@login_required
def analytics_report(request):
    return render(request, "admin_panel/analytics_report.html")


@login_required
def announcement(request):
    return render(request, "admin_panel/announcement.html")


@login_required
def enquiry(request):
    return render(request, "admin_panel/enquiry.html")


@login_required
def settings(request):
    return render(request, "admin_panel/settings.html")
