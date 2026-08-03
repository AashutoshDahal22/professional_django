from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse

# Create your views here.

#redirect
def welcome(request):
    return redirect("home")

def home(request):
    print(request)
    # return HttpResponse("Welcome")

    #to display the html
    return render(request,"home.html")
    
    #to display the data using inline html
    # return HttpResponse("""
    #     <h1>StudentHub</h1>

    #     <p>Welcome Students!</p>
    # """)

def about(request):
    return HttpResponse("about-you")

    #implement the rendered html here
    #take reference from the home() function if needed

def contact(request):
    # return HttpResponse("your-contact-info")

    #implement the rendered html here
    #take reference from the home() function if needed
    return render(request,"contact.html")

def student(request,id):
    return HttpResponse(f"Student ID: {id}")

def student_info(request,id,name):
    return HttpResponse(f"Student ID: {id} Student Name: {name}")

def search(request):

    # print(request.method)

    # print(request.GET)

    # print(request.path)

    # print(request.headers)

    name=request.GET.get("name")
    return HttpResponse(f"Searching for name: {name}")

def login(request):
    
    print("Method :", request.method)

    print("GET :", request.GET)

    print("POST :", request.POST)

    if request.method == "POST":

        username = request.POST.get("username")

        return HttpResponse(f"Welcome {username}")
    
    elif(request.method=="GET"):
        pass;

    return render(request,"login.html")


# Class Based Login View
class LoginView(View):

    def get(self, request):

        print("Method :", request.method)
        print("GET :", request.GET)
        print("POST :", request.POST)

        return render(request, "login.html")

    def post(self, request):

        print("Method :", request.method)
        print("GET :", request.GET)
        print("POST :", request.POST)

        username = request.POST.get("username")

        return HttpResponse(f"Welcome {username} (CBV)")