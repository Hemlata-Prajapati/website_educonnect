from django.urls import path
from . import views

urlpatterns = [
    path("login/<str:role>/", views.role_login, name="role_login"),
    path("register/<str:role>/", views.role_register, name="role_register"),
    path("logout/", views.user_logout, name="logout"),
]
