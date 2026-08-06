from django.shortcuts import redirect, render

from .forms import ContactForm
from .models import Students

# Create your views here.


# if the welcome url is hit it REDIRECTS us to the home page
def welcome(request):
    return redirect("home")


# this is the home page returns a HTML template
def home(request):

    # to disply only one student data
    data = Students.objects.get(id=1)

    # data into the HTML template is fetch using the DJANGO ORM using GET method

    return render(request, "home.html", {"students": data})


def about(request):
    return render(request, "about.html")


def contact(request):

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            # if not using model forms
            # Contact.objects.create(
            #     name=form.cleaned_data["name"],
            #     email=form.cleaned_data["email"],
            #     age=form.cleaned_data["age"],
            #     subject=form.cleaned_data["subject"],
            #     message=form.cleaned_data["message"],
            # )

            # if using model forms
            form.save()

            return render(
                request, "contact.html", {"form": ContactForm(), "success": True}
            )

    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})


def student(request):

    data = Students.objects.all()  # fetches all students

    # select related usage
    # this fetches the students data with the course data such that we don't have to go back and forth between the student and the course table
    # students = Students.objects.select_related("course")

    return render(request, "students.html", {"students": data})
