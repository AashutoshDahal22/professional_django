# Common Django Beginner Mistakes and Their Solutions

> A practical troubleshooting guide for beginners learning Django.

---

# 1. Virtual Environment (venv) Not Activated

## Problem

Running commands without activating the virtual environment.

```bash
python manage.py runserver
```

Error:

```
ModuleNotFoundError: No module named 'django'
```

## Why it happens

The terminal is using your system Python instead of the virtual environment where Django is installed.

## Solution

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

Verify:

```bash
where python
```

or

```bash
which python
```

The path should point inside your virtual environment.

---

# 2. Closing the Terminal After Activating venv

## Problem

You activated the environment, closed the terminal, opened a new one, and Django no longer works.

## Why it happens

Activation only lasts for the current terminal session.

## Solution

Every new terminal requires:

```bash
venv\Scripts\activate
```

before using Django commands.

---

# 3. Opening a Different Terminal

## Problem

One terminal has the venv activated.

Another terminal does not.

Commands work in one terminal but fail in another.

## Solution

Activate the virtual environment separately in every terminal.

---

# 4. Opening the Wrong Folder in VS Code

## Problem

Opening only the app folder.

Example

```
myproject/
    manage.py
    myapp/
```

Instead of opening **myproject**, you opened **myapp**.

## Symptoms

- manage.py not found
- Cannot run migrations
- Import errors

## Solution

Always open the folder containing

```
manage.py
```

---

# 5. Running Commands in the Wrong Directory

## Problem

You're inside

```
myapp/
```

instead of

```
project/
```

and run

```bash
python manage.py runserver
```

Error

```
manage.py not found
```

## Solution

Navigate back.

```bash
cd ..
```

Confirm

```bash
dir
```

or

```bash
ls
```

You should see

```
manage.py
```

---

# 6. Editing the Wrong urls.py

## Problem

There are two urls.py files.

```
project/
    urls.py

app/
    urls.py
```

The beginner edits the wrong one.

## Solution

Remember:

Project urls.py

- Connects apps

App urls.py

- Contains app routes

---

# 7. Editing the Wrong settings.py

## Problem

Creating another settings.py accidentally or editing a copied file.

## Solution

Only edit

```
project/settings.py
```

---

# 8. Forgetting to Add App in INSTALLED_APPS

## Error

```
No installed app with label ...
```

## Solution

Add

```python
INSTALLED_APPS = [
    ...
    "myapp",
]
```

---

# 9. Forgetting include()

Example

```python
path("", myapp.urls)
```

instead of

```python
path("", include("myapp.urls"))
```

## Error

```
TypeError
```

## Solution

Import include.

```python
from django.urls import include
```

---

# 10. Forgetting to Create app urls.py

Only project urls.py exists.

## Solution

Create

```
myapp/
    urls.py
```

---

# 11. Forgetting __init__.py

## Problem

Deleting it because "it's empty."

## Solution

Never delete

```
__init__.py
```

It tells Python this is a package.

---

# 12. Not Saving the File

## Problem

Running the server after making changes.

Nothing changes.

## Solution

Save

```
Ctrl + S
```

before refreshing.

---

# 13. Browser Cache Confusion

## Problem

Changes don't appear.

## Solution

Hard refresh.

```
Ctrl + Shift + R
```

---

# 14. Forgetting to Restart the Server (Sometimes)

Some configuration changes require restarting.

## Solution

Stop server

```
Ctrl + C
```

Run

```bash
python manage.py runserver
```

again.

---

# 15. Running migrate Before makemigrations

Wrong

```bash
python manage.py migrate
```

Correct

```bash
python manage.py makemigrations

python manage.py migrate
```

---

# 16. Editing Models Without Migrating

## Symptoms

Database doesn't update.

## Solution

Run

```bash
python manage.py makemigrations

python manage.py migrate
```

---

# 17. Deleting Migration Files

## Problem

Deleting migrations randomly.

## Result

Database inconsistency.

## Solution

Never delete migrations unless you know what you're doing.

---

# 18. Forgetting to Create Superuser

Trying to login to admin.

No account exists.

## Solution

```bash
python manage.py createsuperuser
```

---

# 19. Forgetting to Register Models in admin.py

## Problem

Models don't appear in Django Admin.

## Solution

```python
from django.contrib import admin
from .models import Contact

admin.site.register(Contact)
```

---

# 20. Using Project Templates Folder Incorrectly

## Problem

Putting templates everywhere.

## Solution

Choose one approach.

Either

```
templates/
```

or

```
app/templates/
```

Remain consistent.

---

# 21. Typing the Wrong App Name

Example

```python
INSTALLED_APPS = [
    "contacts"
]
```

Actual app

```
contact
```

## Solution

Names must match exactly.

---

# 22. Wrong Indentation

Python requires indentation.

Example

```python
def home(request):
return render(request,"home.html")
```

Error

```
IndentationError
```

Solution

```python
def home(request):
    return render(request,"home.html")
```

---

# 23. Using Tabs and Spaces Together

## Error

```
TabError
```

## Solution

Use only spaces (PEP 8 recommends 4 spaces).

Configure VS Code to insert spaces instead of tabs.

---

# 24. Typing the Wrong URL

Example

```
localhost:8000/home
```

instead of

```
localhost:8000/home/
```

## Solution

Match the URL pattern exactly.

---

# 25. Forgetting Trailing Slash

Route

```python
path("about/", ...)
```

User visits

```
/about
```

Usually Django redirects.

Some APIs won't.

---

# 26. Incorrect Template Path

Wrong

```python
render(request,"homepage.html")
```

File

```
home.html
```

Error

```
TemplateDoesNotExist
```

---

# 27. Wrong Static File Path

Wrong

```html
<img src="images/logo.png">
```

Correct

```html
{% load static %}

<img src="{% static 'images/logo.png' %}">
```

---

# 28. Forgetting {% load static %}

Error

```
Invalid block tag 'static'
```

Solution

```django
{% load static %}
```

---

# 29. Forgetting CSRF Token

POST form

```html
<form method="POST">
```

Missing

```django
{% csrf_token %}
```

Error

```
403 Forbidden
CSRF verification failed
```

---

# 30. Using GET Instead of POST

Wrong

```html
<form method="GET">
```

when submitting passwords or data.

Solution

Use

```html
method="POST"
```

---

# 31. Forgetting request.POST

Wrong

```python
name = request.GET["name"]
```

Form uses POST.

Correct

```python
request.POST["name"]
```

---

# 32. Accessing request.POST Before Submission

Wrong

```python
request.POST["name"]
```

without checking method.

Solution

```python
if request.method == "POST":
```

---

# 33. Using request.POST Instead of request.FILES

File uploads require

```python
request.FILES
```

---

# 34. Forgetting enctype for File Uploads

Missing

```html
enctype="multipart/form-data"
```

Uploaded file becomes empty.

---

# 35. Not Running collectstatic (Production)

Only needed in deployment.

---

# 36. Editing Database Directly

Changing SQLite manually.

Can break migrations.

Use Django ORM instead.

---

# 37. Deleting db.sqlite3 Randomly

Can lose all data.

Only delete intentionally when resetting development.

---

# 38. Confusing Project and App

Project

- Settings
- URLs
- Configuration

App

- Models
- Views
- Templates
- Business logic

---

# 39. Multiple Apps With Same Template Names

Both apps have

```
home.html
```

Django may load the wrong one.

Solution

Use

```
templates/appname/home.html
```

---

# 40. Using Relative Imports Incorrectly

Wrong

```python
import models
```

Correct

```python
from .models import Contact
```

---

# 41. Renaming Files Without Updating Imports

Rename

```
views.py
```

Imports still point to old names.

Update all imports.

---

# 42. Installing Packages Outside the Virtual Environment

Package installs globally.

Project cannot find it.

Always activate venv first.

---

# 43. Forgetting to Freeze Requirements

Others clone the project.

Packages missing.

Solution

```bash
pip freeze > requirements.txt
```

---

# 44. Using Different Python Versions

Example

System Python

```
3.13
```

Virtual Environment

```
3.11
```

Can create compatibility issues.

Keep versions consistent.

---

# 45. Ignoring Error Messages

Beginners often read only the last line.

Instead:

- Read the entire traceback.
- Identify the first file in your project where the error occurs.
- Focus on the exception type and message.

---

# 46. Forgetting to Activate Auto Save (Optional)

Frequent issue during development.

Enable VS Code Auto Save:

```
File
→ Auto Save
```

---

# 47. Forgetting to Select the Correct Python Interpreter

VS Code may use the system Python instead of the virtual environment.

## Solution

- Press `Ctrl + Shift + P`
- Search for **Python: Select Interpreter**
- Choose the interpreter inside your virtual environment (venv).

---

# 48. Confusing `python` and `py` on Windows

Some systems use:

```bash
python manage.py runserver
```

Others require:

```bash
py manage.py runserver
```

Use whichever launches your intended Python interpreter.

---

# 49. Using Incorrect File Names

Common mistakes:

- `View.py` instead of `views.py`
- `Model.py` instead of `models.py`
- `Template` instead of `templates`

Django expects specific filenames.

---

# 50. Panic-Fixing Errors Without Reading Them

A common beginner habit is repeatedly changing code, reinstalling packages, or deleting files without understanding the error.

## Better Approach

1. Read the full traceback.
2. Identify the exception type.
3. Locate the first error in your own code.
4. Fix one issue at a time.
5. Test again.

This systematic approach is faster and prevents introducing new problems.

---

# Quick Troubleshooting Checklist

Before asking for help, check the following:

- [ ] Virtual environment activated
- [ ] Correct Python interpreter selected
- [ ] Opened the project folder (contains `manage.py`)
- [ ] Running commands from the correct directory
- [ ] Saved all files
- [ ] Added app to `INSTALLED_APPS`
- [ ] Included app URLs in `project/urls.py`
- [ ] Ran `makemigrations` after model changes
- [ ] Ran `migrate`
- [ ] Registered models in `admin.py`
- [ ] Restarted the development server if necessary
- [ ] Included `{% csrf_token %}` in POST forms
- [ ] Used `{% load static %}` for static files
- [ ] Read the complete error traceback before making changes

---

## Final Advice

Almost every Django beginner encounters these issues. Most are not caused by Django itself but by:
- Working in the wrong directory
- Using the wrong Python environment
- Forgetting migrations
- Misunderstanding the distinction between the **project** and an **app**
- Skipping or misreading error messages

Developing the habit of checking your environment, reading tracebacks carefully, and understanding the project structure will resolve the majority of beginner problems.