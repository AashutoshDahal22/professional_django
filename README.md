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
