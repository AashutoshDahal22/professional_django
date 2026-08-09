from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render

from .forms import RegisterForm


def register(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect("home")

    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})


def user_login(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect("home")

        return render(
            request, "accounts/login.html", {"error": "Invalid username or password."}
        )

    return render(request, "accounts/login.html")


@login_required
def user_logout(request):

    if request.method == "POST":
        logout(request)

        return redirect("login")

    return redirect("home")


@login_required
def profile(request):

    return render(request, "accounts/profile.html")


@login_required
def teacher_dashboard(request):

    is_teacher = request.user.groups.filter(name="Teacher").exists()

    if not is_teacher:
        return HttpResponseForbidden("You do not have permission to access this page.")

    return render(request, "accounts/teacher_dashboard.html")
