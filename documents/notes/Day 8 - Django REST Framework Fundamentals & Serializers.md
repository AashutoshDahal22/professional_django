# Class 8 — Django REST Framework Fundamentals & Serializers

# 1. What is an API?

API stands for:

> **Application Programming Interface**

An API allows two software systems to communicate with each other.

For example:

```text
React Frontend
      |
      | HTTP Request
      ↓
Django REST API
      |
      ↓
Database
```

The frontend does not directly access the database.

Instead:

```text
Frontend → API → Database
```

The API acts as a communication layer between the client and server.

---

# 2. Traditional Django vs REST API

Students have already worked with Django templates.

Traditional Django:

```text
Browser
   ↓
Django View
   ↓
Database
   ↓
Django Template
   ↓
HTML
   ↓
Browser
```

With DRF:

```text
React / Mobile App / Postman
             ↓
         HTTP Request
             ↓
        Django REST API
             ↓
          Database
             ↓
        Serializer
             ↓
          JSON
             ↓
         Client
```

The major difference:

### Traditional Django

The server usually returns:

```html
<h1>Students</h1>
<p>Aashutosh</p>
```

### REST API

The server usually returns:

```json
{
  "id": 1,
  "name": "Aashutosh",
  "age": 22
}
```

The client decides how to display that data.

---

# 3. Why REST API?

REST APIs are useful because the backend can serve multiple clients.

For example:

```text
                 ┌── React Web App
                 │
Django REST API ─┼── Mobile App
                 │
                 ├── Desktop App
                 │
                 └── Third-party Application
```

The same backend API can be consumed by different applications.

### Advantages

- Separation between frontend and backend
- Supports multiple clients
- Lightweight data exchange
- Usually uses JSON
- Easy to consume using HTTP
- Works well with React, Vue, Angular, mobile apps, etc.
- Easy to test using tools such as Postman

---

# 4. REST

REST stands for:

> **Representational State Transfer**

REST is an architectural style for designing network APIs.

REST APIs generally use:

- Resources
- HTTP methods
- HTTP status codes
- URLs
- Representations such as JSON

---

# 5. REST Resources

In REST, we usually think about data as **resources**.

For a student application:

```text
Student
Course
Teacher
Department
```

The URL represents the resource.

For example:

```text
/api/students/
```

represents the collection of students.

```text
/api/students/1/
```

represents one particular student.

---

# 6. RESTful Architecture

A RESTful API commonly follows these ideas:

### 1. Client-Server

Client and server have separate responsibilities.

```text
Client                  Server
React     ← HTTP →      Django API
```

### 2. Stateless

Each request should contain the information necessary for the server to process it.

The server should not depend on previous requests to understand the current request.

### 3. Uniform Interface

Resources are accessed through consistent URLs and HTTP methods.

Example:

```text
GET    /api/students/
POST   /api/students/
GET    /api/students/1/
PUT    /api/students/1/
PATCH  /api/students/1/
DELETE /api/students/1/
```

### 4. Resource-Based

URLs represent resources.

Good:

```text
/api/students/
```

Less RESTful:

```text
/api/getStudents/
```

The HTTP method already tells us the operation.

---

# 7. HTTP Methods

HTTP methods tell the server what the client wants to do.

| Method | Purpose                           |
| ------ | --------------------------------- |
| GET    | Read data                         |
| POST   | Create data                       |
| PUT    | Replace/update an entire resource |
| PATCH  | Partially update a resource       |
| DELETE | Delete data                       |

Example:

```text
GET /api/students/
```

Means:

> Give me the students.

```text
POST /api/students/
```

Means:

> Create a new student.

```text
GET /api/students/1/
```

Means:

> Give me student with ID 1.

```text
PUT /api/students/1/
```

Means:

> Replace/update student 1.

```text
PATCH /api/students/1/
```

Means:

> Update some fields of student 1.

```text
DELETE /api/students/1/
```

Means:

> Delete student 1.

---

# 8. API Endpoints

An endpoint is a specific URL through which an API resource can be accessed.

For students:

```text
/api/students/
```

Collection endpoint.

```text
/api/students/1/
```

Individual resource endpoint.

Our API design:

```text
GET       /api/students/
POST      /api/students/

GET       /api/students/1/
PUT       /api/students/1/
PATCH     /api/students/1/
DELETE    /api/students/1/
```

Important:

The URL and HTTP method work together.

For example:

```text
GET /api/students/
```

and

```text
POST /api/students/
```

are different operations even though they use the same URL.

---

# 9. JSON

JSON stands for:

> JavaScript Object Notation

It is a common format for exchanging data between client and server.

Example:

```json
{
  "id": 1,
  "name": "Aashutosh",
  "age": 22,
  "course": "Django"
}
```

JSON supports:

- Strings
- Numbers
- Booleans
- Arrays
- Objects
- null

Example:

```json
{
  "name": "Aashutosh",
  "age": 22,
  "is_active": true,
  "skills": ["Python", "Django", "React"]
}
```

---

# 10. HTTP Status Codes

Status codes tell the client what happened with the request.

### 2xx — Success

```text
200 OK
201 Created
204 No Content
```

Common examples:

```text
GET successful → 200
POST successful → 201
DELETE successful → 204
```

### 4xx — Client Error

```text
400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
```

Examples:

```text
Invalid data → 400
Not authenticated → 401
No permission → 403
Student does not exist → 404
```

### 5xx — Server Error

```text
500 Internal Server Error
```

This generally means something went wrong on the server.

---

# 11. What is Django REST Framework?

Django REST Framework, commonly called **DRF**, is a toolkit for building Web APIs using Django.

Django already provides:

- URL routing
- Views
- Models
- ORM
- Authentication
- Middleware

DRF adds API-specific functionality such as:

- Serializers
- API views
- Response objects
- Authentication
- Permissions
- Generic views
- ViewSets
- Routers
- API testing interface

---

# 12. Installing DRF

Install:

```bash
pip install djangorestframework
```

Check installation:

```bash
pip show djangorestframework
```

---

# 15. Configure DRF

Add DRF to `INSTALLED_APPS`.

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "rest_framework",

    "students",
]
```

---

# 13. Recommended Project Structure

For today's practical:

```text
project/
│
├── manage.py
│
├── project/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
└── students/
    ├── migrations/
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── serializers.py
    ├── urls.py
    ├── views.py
    └── ...
```

Important new file:

```text
serializers.py
```

This is where serializer classes are usually placed.

---

# 14. API Request/Response Lifecycle

A basic DRF request looks like this:

```text
Client
   ↓
HTTP Request
   ↓
URL
   ↓
APIView
   ↓
Serializer
   ↓
Model / Database
   ↓
Serializer
   ↓
Response
   ↓
JSON
   ↓
Client
```

For a GET request:

```text
GET /api/students/

        ↓

URL matches view

        ↓

APIView

        ↓

Student.objects.all()

        ↓

Serializer

        ↓

Python/Django objects → JSON-compatible data

        ↓

Response

        ↓

JSON returned to client
```

For POST:

```text
Client sends JSON
        ↓
APIView
        ↓
Serializer
        ↓
Validation
        ↓
Save to database
        ↓
Serializer
        ↓
Response
```

This lifecycle is one of the most important concepts of today's class.

---

# 15. APIView

`APIView` is one of the fundamental DRF view classes.

It allows us to handle HTTP methods separately.

Example:

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class StudentAPIView(APIView):

    def get(self, request):
        return Response({
            "message": "GET request"
        })

    def post(self, request):
        return Response({
            "message": "POST request"
        })
```

The method names correspond to HTTP methods:

```text
GET     → get()
POST    → post()
PUT     → put()
PATCH   → patch()
DELETE  → delete()
```

---

# 16. Response

DRF provides the `Response` class.

```python
from rest_framework.response import Response
```

Instead of:

```python
return JsonResponse(data)
```

we commonly use:

```python
return Response(data)
```

Example:

```python
return Response({
    "message": "Student created"
})
```

---

# 17. Status

DRF provides readable HTTP status constants.

```python
from rest_framework import status
```

Instead of:

```python
return Response(data, status=200)
```

we can write:

```python
return Response(
    data,
    status=status.HTTP_200_OK
)
```

Examples:

```python
status.HTTP_200_OK
status.HTTP_201_CREATED
status.HTTP_204_NO_CONTENT
status.HTTP_400_BAD_REQUEST
status.HTTP_404_NOT_FOUND
```

This makes the code easier to understand.

---

# 18. What is Serialization?

Serialization means converting complex Python/Django data into a format that can be easily transmitted.

For example:

```text
Django Model Object
        ↓
    Serializer
        ↓
Dictionary / JSON-compatible data
```

Example:

```python
student = Students.objects.get(id=1)
```

The object might look conceptually like:

```text
Students object
name = "Aashutosh"
age = 22
course = "Django"
```

A serializer converts it into:

```python
{
    "id": 1,
    "name": "Aashutosh",
    "age": 22,
    "course": "Django"
}
```

Which can then be returned as JSON.

---

# 19. Serialization vs Deserialization

### Serialization

```text
Model Object
     ↓
Serializer
     ↓
Python dictionary
     ↓
JSON response
```

### Deserialization

The opposite direction:

```text
JSON request
     ↓
Serializer
     ↓
Validated Python data
     ↓
Django Model
     ↓
Database
```

So:

```text
Serialization
Python → API representation

Deserialization
API representation → Python/data
```

---

# 20. Serializer

A basic DRF serializer can be created using:

```python
from rest_framework import serializers
```

Example:

```python
class StudentSerializer(serializers.Serializer):

    name = serializers.CharField()
    age = serializers.IntegerField()
    email = serializers.EmailField()
```

This defines the structure of the API data.

---

# 21. Serializer Fields

Common serializer fields include:

```python
serializers.CharField()
serializers.IntegerField()
serializers.EmailField()
serializers.BooleanField()
serializers.DateField()
serializers.DateTimeField()
serializers.DecimalField()
```

Example:

```python
class StudentSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    email = serializers.EmailField()
    is_active = serializers.BooleanField()
```

---

# 22. ModelSerializer

When working with Django models, manually defining every field can become repetitive.

DRF provides:

> `ModelSerializer`

Example model:

```python
class Student(models.Model):

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
```

Serializer:

```python
from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"
```

DRF automatically creates serializer fields based on the model.

---

# 23. ModelSerializer Concept

Without `ModelSerializer`:

```text
Django Model
     ↓
Manually define serializer fields
     ↓
Serializer
```

With `ModelSerializer`:

```text
Django Model
     ↓
ModelSerializer
     ↓
Fields generated automatically
```

This is why `ModelSerializer` is commonly used in CRUD APIs.

---

# 24. Selecting Specific Fields

Instead of:

```python
fields = "__all__"
```

we can specify:

```python
class Meta:
    model = Student
    fields = [
        "id",
        "name",
        "age",
        "email",
    ]
```

This is useful when we don't want every model field exposed through the API.

---

# 25. Read-Only Fields

A read-only field can be returned by the API but should not be provided/modified by the client.

Example:

```python
class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ["id", "name", "age"]
        read_only_fields = ["id"]
```

The client can receive:

```json
{
  "id": 1,
  "name": "Aashutosh",
  "age": 22
}
```

But the client should not control the ID.

---

# 26. Write-Only Fields

A write-only field can be sent to the API but is not returned in responses.

A common example is a password.

```python
password = serializers.CharField(write_only=True)
```

Conceptually:

```text
Client → password → API
```

But:

```text
API → password → Client
```

should not happen.

This becomes especially important when we work with authentication.

---

# 27. Nested Serializers — Introduction

Nested serializers allow one serializer to represent related data.

Suppose:

```text
Student
   ↓
Course
```

A simple response might be:

```json
{
  "id": 1,
  "name": "Aashutosh",
  "course": 2
}
```

A nested representation could instead be:

```json
{
  "id": 1,
  "name": "Aashutosh",
  "course": {
    "id": 2,
    "name": "Django"
  }
}
```

Example:

```python
class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ["id", "name"]


class StudentSerializer(serializers.ModelSerializer):

    course = CourseSerializer()

    class Meta:
        model = Student
        fields = ["id", "name", "age", "course"]
```

For today's class, only introduce the concept.

Detailed nested serializer handling can be covered later during the project.

---

# 28. Building the Student API

Assume we already have:

```python
class Student(models.Model):

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
```

---

# 29. Create `serializers.py`

```python
from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"
```

---

# 30. First API — GET Students

```python
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Student
from .serializers import StudentSerializer


class StudentAPIView(APIView):

    def get(self, request):

        students = Student.objects.all()

        serializer = StudentSerializer(
            students,
            many=True
        )

        return Response(serializer.data)
```

Important:

```python
many=True
```

is used because we are serializing multiple objects.

---

# 31. Single Student

For:

```text
/api/students/1/
```

we need an ID.

```python
class StudentDetailAPIView(APIView):

    def get(self, request, pk):

        student = Student.objects.get(pk=pk)

        serializer = StudentSerializer(student)

        return Response(serializer.data)
```

Here:

```python
pk
```

represents the primary key.

---

# 32. API URLs

`students/urls.py`

```python
from django.urls import path

from .views import (
    StudentAPIView,
    StudentDetailAPIView,
)


urlpatterns = [

    path(
        "students/",
        StudentAPIView.as_view(),
        name="student-list"
    ),

    path(
        "students/<int:pk>/",
        StudentDetailAPIView.as_view(),
        name="student-detail"
    ),

]
```

Project URL:

```python
from django.urls import include, path


urlpatterns = [
    path(
        "api/",
        include("students.urls")
    ),
]
```

Now:

```text
/api/students/
/api/students/1/
```

---

# 33. GET Request

Request:

```http
GET /api/students/
```

Response:

```json
[
  {
    "id": 1,
    "name": "Aashutosh",
    "age": 22,
    "email": "aashutosh@example.com"
  },
  {
    "id": 2,
    "name": "Ram",
    "age": 21,
    "email": "ram@example.com"
  }
]
```

---

# 34. POST Request

Now we want to create a student.

```python
class StudentAPIView(APIView):

    def get(self, request):

        students = Student.objects.all()

        serializer = StudentSerializer(
            students,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):

        serializer = StudentSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
```

Import:

```python
from rest_framework import status
```

---

# 35. POST Request Flow

When the client sends:

```json
{
  "name": "Ram",
  "age": 21,
  "email": "ram@example.com"
}
```

The flow is:

```text
POST request
      ↓
request.data
      ↓
Serializer
      ↓
is_valid()
      ↓
Validation
      ↓
serializer.save()
      ↓
Database
      ↓
Response
```

---

# 36. Why `is_valid()`?

Before saving client-provided data, we should validate it.

```python
serializer.is_valid()
```

If valid:

```python
serializer.save()
```

If invalid:

```python
serializer.errors
```

Example:

```json
{
  "email": ["Enter a valid email address."]
}
```

Detailed serializer validation will be covered in **Class 9**.

---

# 37. PUT and PATCH

For updating:

```text
PUT /api/students/1/
```

and:

```text
PATCH /api/students/1/
```

The serializer receives the existing object and incoming data.

Conceptually:

```python
serializer = StudentSerializer(
    student,
    data=request.data
)
```

For partial update:

```python
serializer = StudentSerializer(
    student,
    data=request.data,
    partial=True
)
```

The important difference:

### PUT

Usually represents a complete update.

### PATCH

Represents a partial update.

Example PATCH:

```json
{
  "age": 23
}
```

Only the age needs to be changed.

---

# 41. DELETE

Delete:

```text
DELETE /api/students/1/
```

Conceptually:

```python
student.delete()

return Response(
    status=status.HTTP_204_NO_CONTENT
)
```

---

# 38. Final API Design

By the end of today's practical, students should understand this structure:

```text
Students API

GET       /api/students/
POST      /api/students/

GET       /api/students/1/
PUT       /api/students/1/
PATCH     /api/students/1/
DELETE    /api/students/1/
```

| Method | Endpoint           | Purpose          |
| ------ | ------------------ | ---------------- |
| GET    | `/api/students/`   | List students    |
| POST   | `/api/students/`   | Create student   |
| GET    | `/api/students/1/` | Get one student  |
| PUT    | `/api/students/1/` | Update student   |
| PATCH  | `/api/students/1/` | Partially update |
| DELETE | `/api/students/1/` | Delete student   |

---
