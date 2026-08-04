from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse

# Create your views here.

#redirect
def welcome(request):
    return redirect("home")

def home(request):
    #to display the dynamic data
    # data={
    #     "name":"Hari",
    #     "course":"BSc CSIT",
    #     "semester":5
    # }
    # return render(request,"home.html",{"data":data})
    return render(request, "home.html", {
            "name": "Aashutosh",
            "logged_in": True
        })

def about(request):
    return render(request,"about.html")


def contact(request):
    return render(request,"contact.html")

def student(request):

    students = [
        {
            "name": "Ram",
            "age": 20,
            "course": "BSc CSIT"
        },
        {
            "name": "Hari",
            "age": 21,
            "course": "BCA"
        },
        {
            "name": "Sita",
            "age": 19,
            "course": "BIT"
        }
    ]

    return render(request, "students.html", {
        "students": students
    })

def student_info(request,id,name):
    return HttpResponse(f"Student ID: {id} Student Name: {name}")

def search(request):
    name=request.GET.get("name")
    return HttpResponse(f"Searching for name: {name}")

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        return HttpResponse(f"Welcome {username}")
    elif(request.method=="GET"):
        pass;
    return render(request,"login.html")


# Class Based Login View
class LoginView(View):

    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        username = request.POST.get("username")
        return HttpResponse(f"Welcome {username} (CBV)")