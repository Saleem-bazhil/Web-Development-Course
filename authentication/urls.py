from django.urls import path, include
from .views import *

urlpatterns = [
    path("", Loginpage),
    path("logout/", Logoutuser),
    path("signup/", Signup),
    path("email/", email),
]
