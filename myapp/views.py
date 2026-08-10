from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import ContactForm
from .models import Contact, Students

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
        form = ContactForm(request.POST, request.FILES)

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


@login_required
def student(request):

    # Normal query
    # Fetches students first.
    students = Contact.objects.all()

    # select_related()
    # Suitable for ForeignKey relationships.
    # Student + Course are fetched using a SQL JOIN.
    # students_select = Students.objects.select_related("course")

    # prefetch_related()
    # Django performs separate queries and joins the
    # results in Python.
    # students_prefetch = Students.objects.prefetch_related("course")

    return render(
        request,
        "students.html",
        {
            "students": students,
            # "students_select": students_select,
            # "students_prefetch": students_prefetch,
        },
    )
