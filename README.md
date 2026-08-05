## Introduction

How does a social media shows posts?

- Backend Framework or Django
  - It is the backend that sits between the user and the db

> Django is a high-level Python web framework used for building web applications quickly, securely, and with clean architecture.

> A web framework is a pre-written collection of code, tools, and rules that helps developers build websites and web apps quickly without starting from scratch.

_Can we not make websites or backends using django?_

- Yes, we can using Nodejs, Java and other different frameworks but Django provides something they generally fail to provide.

**Why Django?**

- Rapid Development
- Security
- Scalable

_Django is oftern known as **Batteries Included Framework** meaning everything is packaged and often provided in Django_

## THE MVT architecture

![[Pasted image 20260802065212.png]]

M = Model = Responsible For Data

- Example
  - Student, Name , Age Email to be stored into the db

V = Views = Business Logics

- Example
  - Student Clicks `/students`
  - View Decides
    - _Fetch Students_
    - _Sort Students_
    - _Send Students_

T = Template = Display to user via HTML

_Possible Question?_

- Why can't we show view directly into **HTML**?
  - because business logic and design should stay seperate

## Django Project VS Django Application

Django Project

- Entire Website
  - Amazon
  - Facebook

Django Application

- One functionality/module/artifact
  - Products
  - Payments
  - Authentication

_One Analogy_

Project = Shopping Mall
App = Individual Shops/Parking,etc

## Virtual Environment

- Problem
  - Project A
    - Django v1
  - Project B
    - Django v2

> Without virtual environment creates conflicts

> With virtual environment it creates isolated _Python environment_
> _with this it creates its own packages, versions, dependencies_

### Commands

`python -m venv yourvenvname`
Windows
`yourvenvname\Scripts\activate`
Unix
`source yourvenvname/bin/activate`

Install Django
`pip install django`

Create Django Project
`django-admin startproject yourprojectname .`
Create App
`python manage.py startapp yourappname`
Runserver
`python manage.py runserver`
`python3 manage.py runserver`
`py manage.py runserver`

## Explaning the files

- manage.py
  - command center
    - runserver
    - migrate
    - createsuperuser
    - shell
    - startapp
- settings.py
  - entire configuration
    - Installed apps
    - db
    - language
    - timezone
    - security
    - templates
    - middleware
- urls.py
  - maps URLs to View
- wsgi.py
  - used for deployment
    - WSGI = Web Server Gateway Interface
  - allows django to communicate with webservers
  - not touched in development
- asgi.py
  - modern version
    - websockets
    - async views
    - realtime chat
    - notification

_Difference between WSGI and ASGI_
WSGI

```
Synchronous

One request at a time
```

ASGI

```
Asynchronous

Many concurrent requests

WebSockets
```

## Day 2 - URL Routing, Views & HTTP Requests

> URL routing is the process of matching an incoming web address (URL) to a specific function, file, or view inside a web application

>A **URL Pattern** is an individual rule inside `urlpatterns` that tells Django which view should handle a particular URL.

>A **Named URL** assigns a unique name to a URL pattern so you can refer to it without writing the actual URL.

>A **URL Parameter** is a value captured from the URL and passed into the view as an argument.

>A **Dynamic URL** is a URL whose path changes depending on values supplied by the user.

>A **URL Namespace** groups URL names by application so that different apps can safely use the same URL names.

|Concept|Purpose|Example|
|---|---|---|
|URL Routing|Directs requests to the correct view|`/about/ → about()`|
|URL Pattern|A single routing rule|`path("about/", views.about)`|
|Named URL|Gives a URL a reusable name|`name="about"`|
|URL Parameter|Captures values from the URL|`<int:id>`|
|Dynamic URL|Uses parameters to handle many URLs with one pattern|`/student/5/`|
|URL Namespace|Prevents URL name conflicts between apps|`blog:home`, `shop:home`|

How to make *Git Bash* as default terminal?
- `Ctrl + Shift + P` 
- Search for *Terminal: Select Default Profile*
- Select *GIt Bash*
- If *Git Bash* not available then install *Git* and set-up as we need it for the project later on

## Day 3 - Template, Template Language and Static Files


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
### Database Concepts
- Until now when we close the program, our data disappears or the data is not saved
- Database solves this problem ==A database is simply an organized collection of data that can be stored, searched, updated, and deleted whenever needed.==

### Database Terminology
- Table
	- Table is a database concept which stores information.

| ID  | Name  | Age |
| --- | ----- | --- |
| 1   | John  | 20  |
| 2   | Alice | 19  |
- Row(Record)
	- Each student is one row
		- Example
			- John is a row and Alice is a row
- Column(Field)
	- Each property is a column
		- Example
			- Name,Age,Email,PhoneNumber

### Django ORM
***ORM*** stand for *Object Relational Mapper* and is one of the biggest features of Django.

Databases understand SQL but does python understand SQL?
	*Django* acts as a translator and translates one into another i.e SQL to Python and vice versa.
	Without *ORM* we need to write the SQL ourselves.

##### Creating Models
A Model represents one database table.
Every model becomes one table.

***Example***
Student Model
```
Student
```
becomes
Students Table
| ID | Name | Age |

*its like a blueprint for the database table*

##### Model Fields
Fields define what information each record stores.

- Name
- Age
- Email
- Date Joined

Each field has a data type.

##### Common Django Fields

| Field         | Description             | Example              |
| ------------- | ----------------------- | -------------------- |
| CharField     | Stores short text.      | Name                 |
| TextField     | Stores long paragraphs. | Blog Content         |
| IntegerField  | Whole Numbers           | Age                  |
| FloatField    | Decimal numbers.        | Price                |
| BooleanField  | True or False.          | Active               |
| DateField     | Only dates.             | Birthday             |
| DateTimeField | Stores date and time.   | createdAt,Login Time |
| EmailField    | Stores Email Addresses  | email@example.com    |
| ImageField    | Stores image paths.     | Profile Picture      |
| FileField     | Stores uploaded files.  | PDF                  |

##### Primary Keys
- Every table needs a *unique* identifier
Example

| ID  | Name |
| --- | ---- |
| 1   | John |
| 2   | John |
| 3   | John |
Three students have the same name.
How do we know which John is which?
Using the ID.
The ID is called the *Primary Key*.

Django automatically created `id` as the primary key.

##### Default Values

Sometimes users don't provide information.
Instead of leaving it empty,
we provide a default value.
Example
```
Country = Nepal
```
If a new student doesn't enter a country,
it automatically becomes Nepal.

Benefits
- Reduces user input
- Prevents missing values
- Makes data consistent

##### Null vs Blank

| Null                                      | Blank                                                           |
| ----------------------------------------- | --------------------------------------------------------------- |
| Database Level                            | Form Level                                                      |
| The database literally stores<br><br>NULL | It controls whether users are allowed to leave the field empty. |

#### Model Relationships
Real world data is connected. For example

Students belonging to a class,
A book has an autor and much more.

Instead of copying the same information repeatedly, databases create relationships.
Benefits:

- Avoid duplicate data.
- Keep information consistent.
- Make updates easier.

Django provides three main relationship types.

##### Foreign Key(Many to One)
A ForeignKey means **many records can be related to one record**.

Example
`one teacher has many students`

##### OneToOneField(One to One)
One record matches exactly one other record.

Example
`User 1 ------ Profile 1`

##### ManyToManyField
Many records relate to many other records.

Example
`Students can enroll in many courses and course can have many students`

##### SqlLite
SQLite is Django's default database.

It stores everything inside a single file.

Advantages:

- No installation required.
- Easy to set up.
- Perfect for learning and small projects.
- Portable.

Limitations:

- Not ideal for very large applications.
- Limited support for many simultaneous writers.
- Fewer advanced database features.

It is commonly used during development and in small applications.

##### Migrations

A migration is a version-controlled description of changes to your database structure.

If you change a model by adding a field, the database doesn't automatically know about that change.

Migrations keep the model definitions and the database schema synchronized.

Think of them as construction plans.

You update the blueprint (the model), then create and apply a plan to modify the actual building (the database).

##### makemigrations

`makemigrations` compares your current models with the previous state and generates migration files describing the required changes.

It **does not change the database**.

It only creates instructions.

##### migrate

`migrate` reads those migration files and applies the changes to the actual database.

This is when tables are created, altered, or removed.

#### Django ORM Operations (CRUD)

CRUD stands for:

- **Create** – Add new data.
- **Read** – Retrieve existing data.
- **Update** – Modify existing data.
- **Delete** – Remove existing data.

These four operations are the foundation of almost every application.

#### QuerySets
A QuerySet is a collection of database records returned by the ORM.

It represents the result of a query.

Examples:

- All students.
- Students older than 18.
- Students in the Python course.

An important characteristic is that QuerySets are **lazy**.

This means Django does not immediately execute the database query when you create a QuerySet. Instead, it waits until the data is actually needed (for example, when you loop over it or display it). This improves performance because unnecessary database work is avoided.

###### `filter()`

Returns **all records** matching a condition.

Example:

Students with age = 20
###### `get()`

Returns **exactly one record**.

If no record exists, it raises an exception.

If multiple records match, it also raises an exception because it expected only one.

Use `get()` only when you are certain there should be a single result, such as looking up a record by its primary key or a unique email address.

###### `exclude()`

Returns records that **do not** match the condition.

Example:

Instead of showing students from Kathmandu, show students from every other city.

###### `order_by()`

Sorts the results.

Examples:

- Name A → Z
- Name Z → A
- Highest marks first
- Lowest price first
- Newest students first

Ordering only changes the sequence of the results, not the stored data.