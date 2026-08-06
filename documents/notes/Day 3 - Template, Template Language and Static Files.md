## Template, Template Language and Static Files

>The **Django Template Engine** is Django's built-in system for creating dynamic HTML pages. Instead of writing separate HTML files for every possible page, you create **templates** that contain HTML mixed with special Django syntax

```
User
   │
   ▼
Browser Request
   │
   ▼
urls.py
   │
   ▼
views.py
   │
   ▼
Template Engine
   │
Finds HTML Template
   │
Replaces Variables
   │
Processes Tags
   │
   ▼
Final HTML
   │
   ▼
Browser
```

```
<!-- Template Tags

{{ }} for variables

{% %} for logical blocks

{# #} for comments
```

#### Template Filters
> Modifys the output

{{variable|filter}}

Examples:
{{name|upper}}
{{ students|length }}
{{ name|title }}
{{ today|date:"d M Y" }}


The website can have many re-usable components like Navbar ,Logo or Footers.
Do we copy them manually in each page?
No, we use template inheritance.

We create a base.html and enter this code

```html
<html>

<head>

<title>College Portal</title>

</head>

<body>

<nav>


Home

About

Contact

</nav>

{% block content %}

{% endblock %}

<footer>

Copyright

</footer>

</body>

</html>
```

then we can extend this base.html onto other HTML pages.

Then we can keep the **static files** like *css,js and images* into the static folder

base.html with css and enhanced styling
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>{% block title %}Student Management{% endblock %}</title>

    <!-- Bootstrap -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom CSS -->
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>

<body>

<!-- Navbar -->
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container">

        <a class="navbar-brand" href="/">Student Portal</a>

        <div class="navbar-nav ms-auto">
            <a class="nav-link" href="/">Home</a>
            <a class="nav-link" href="/about/">About</a>
            <a class="nav-link" href="/student/">Student</a>
            <a class="nav-link" href="/contact/">Contact</a>
        </div>

    </div>
</nav>

<div class="container mt-5">

    {% block content %}

    {% endblock %}

</div>

<footer class="bg-dark text-white text-center mt-5 p-3">
    © 2026 Student Management System
</footer>

<script src="{% static 'js/script.js' %}"></script>

</body>
</html>
```

base.html without css and js and bootstrap
```html
<html>

  <head>

    <title>College Portal</title>

  </head>

  

  <body>

    <nav>Home About Contact</nav>

  

    {% block content %} {% endblock %}

  

    <footer>Copyright</footer>

  </body>

</html>
```

home.html
```html
{% extends "base.html" %}

{% block title %}
Home
{% endblock %}

{% block content %}

<h1>Welcome {{ name }}</h1>

<p class="lead">
This website is built using Django Templates.
</p>

{% if logged_in %}

<div class="alert alert-success">
    You are successfully logged in.
</div>

{% else %}

<div class="alert alert-warning">
    Please login first.
</div>

{% endif %}

{% endblock %}
```

about.html
```html
{% extends "base.html" %}

{% block title %}
About
{% endblock %}

{% block content %}

<h1>About Us</h1>

<p>
This project demonstrates Django Templates, Template Inheritance,
Static Files, Bootstrap and Template Language.
</p>

<h3>Technologies Used</h3>

<ul>
    <li>Django</li>
    <li>HTML</li>
    <li>CSS</li>
    <li>Bootstrap</li>
    <li>JavaScript</li>
</ul>

{% endblock %}
```

contact.html
```html
{% extends "base.html" %}

{% block title %}
Contact
{% endblock %}

{% block content %}

<h1>Contact Us</h1>

<form>

    <div class="mb-3">

        <label>Name</label>

        <input type="text" class="form-control">

    </div>

    <div class="mb-3">

        <label>Email</label>

        <input type="email" class="form-control">

    </div>

    <div class="mb-3">

        <label>Message</label>

        <textarea class="form-control"></textarea>

    </div>

    <button class="btn btn-primary">
        Send Message
    </button>

</form>

{% endblock %}
```

students.html
```html
{% extends "base.html" %}

{% block title %}
Students
{% endblock %}

{% block content %}

<h1>Students</h1>

<p>Total Students : {{ students|length }}</p>

<table class="table table-bordered table-striped">

    <thead class="table-dark">

    <tr>
        <th>Name</th>
        <th>Age</th>
        <th>Course</th>
    </tr>

    </thead>

    <tbody>

    {% for student in students %}

    <tr>

        <td>{{ student.name }}</td>
        <td>{{ student.age }}</td>
        <td>{{ student.course|upper }}</td>

    </tr>

    {% empty %}

    <tr>

        <td colspan="3">
            No Students Found
        </td>

    </tr>

    {% endfor %}

    </tbody>

</table>

{% endblock %}
```

style.css
```css
body{
    background:#f4f6f8;
}

h1{
    color:#0d6efd;
    margin-bottom:20px;
}

footer{
    margin-top:80px;
}

table{
    background:white;
}
```

script.js
```js
console.log("JavaScript Loaded");

document.addEventListener("DOMContentLoaded", function () {
    alert("Welcome to the Student Management System");
});
```

```python
def home(request):
    return render(request, "home.html", {
        "name": "Aashutosh",
        "logged_in": True
    })


def about(request):
    return render(request, "about.html")


def students(request):

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


def contact(request):
    return render(request, "contact.html")
```

[[Day 4 - Models,Database and Django ORM]]
