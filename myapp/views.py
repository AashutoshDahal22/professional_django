from django.shortcuts import render,redirect
from .models import Students,Contact

# Create your views here.

#redirect
def welcome(request):
    return redirect("home")

def home(request):
    #to disply only one student data
    data=Students.objects.get(id=1)
    
    return render(request,"home.html",{"students":data})

def home_with_dynamicURL(request,id):    
    #to dispalay using dynamic URL
    data=Students.objects.get(id=id)
    
    return render(request,"home.html",{"students":data})

def about(request):
    return render(request,"about.html")


def contact(request):
    if request.method == "POST":

        Contact.objects.create(
            name=request.POST["name"],
            email=request.POST["email"],
            message=request.POST["message"]
        )

        return redirect("/contact/")
    
    return render(request,"contact.html")

def student(request):

    data=Students.objects.all()

    return render(request, "students.html", {
        "students": data
    })