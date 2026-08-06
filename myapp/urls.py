from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("welcome/", views.welcome),  # map
    path("about/", views.about),
    path("contact/", views.contact),
    path("student/", views.student),
]
