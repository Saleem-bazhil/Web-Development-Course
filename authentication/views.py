from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *


# Create your views here.
def Loginpage(request):
    if request.user.is_authenticated:

        return redirect("/inventory/main/")

    context = {"error": ""}

    if request.method == "POST":
        user = authenticate(
            username=request.POST["username"], password=request.POST["password"]
        )
        if user is not None:
            login(request, user)
            return redirect("inventory/main/")
        else:
            context = {"error": "invalid username or password"}
            return render(request, "login.html", context)
    return render(request, "login.html", context)


def Logoutuser(request):
    logout(request)
    return redirect("/")


def Signup(request):
    context = {"error": ""}
    if request.method == "POST":
        user_check = User.objects.filter(username=request.POST["username"])
        if len(user_check) > 0:
            context = {
                "error": "Username Already Exists",
            }
        return render(request, "signup.html", context)
    if request.method == "POST":
        new_user = User(
            username=request.POST["username"],
            first_name=request.POST["firstname"],
            last_name=request.POST["lastname"],
            email=request.POST["email"],
            reference=request.POST["reference"],
            age=request.POST["age"],
        )
        new_user.set_password(request.POST["password"])
        new_user.save()
        return redirect("/")
    return render(request, "signup.html", context)


def email(request):
    context = {"error": ""}

    if request.method == "POST":
        email_value = request.POST.get("email")

        if Email.objects.filter(email=email_value).exists():
            context["error"] = "Email already exists"
            return render(request, "main.html", context)

        if email_value:
            new_email = Email(email=email_value)
            new_email.save()
            return redirect("/inventory/main/")

        context["error"] = "Please enter a valid email."
        return render(request, "footer.html", context)

    return render(request, "main.html")
