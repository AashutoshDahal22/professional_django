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

For more concepts we move on to [[Day 3 - Template, Template Language and Static Files]] in Django.