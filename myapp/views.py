from django.shortcuts import render,redirect
from .models import Students,Contact
from .forms import ContactForm

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

        form = ContactForm(request.POST)

        if form.is_valid():
            
            #if not using model forms
            # Contact.objects.create(
            #     name=form.cleaned_data["name"],
            #     email=form.cleaned_data["email"],
            #     age=form.cleaned_data["age"],
            #     subject=form.cleaned_data["subject"],
            #     message=form.cleaned_data["message"],
            # )

            #if using model forms
            form.save()
            
            return render(
                request,
                "contact.html",
                {
                    "form": ContactForm(),
                    "success": True
                }
            )

    else:

        form = ContactForm()

    return render(
        request,
        "contact.html",
        {
            "form": form
        }
    )

def student(request):

    data=Students.objects.all() #fetches all students

    return render(request, "students.html", {
        "students": data
    })