# Django Forms - Theory Notes

## HTML Forms vs Django Forms

### HTML Forms

HTML forms are created manually using HTML tags such as `<form>`,
`<input>`, `<textarea>`, and `<select>`. The developer is responsible
for handling validation, displaying errors, and processing submitted
data.

### Django Forms

Django Forms are Python classes that generate HTML forms, validate
input, display errors, and provide cleaned data. They reduce repetitive
code and improve security.

------------------------------------------------------------------------

## Django Form Classes

A Django Form class is a Python class that inherits from `forms.Form` or
`forms.ModelForm`. It defines the fields, validation rules, and behavior
of a form.

-   `forms.Form` -- General-purpose forms.
-   `forms.ModelForm` -- Forms linked to a database model.

------------------------------------------------------------------------

## Form Fields

Form fields define the type of data users can enter.

Common fields: - `CharField` - `EmailField` - `IntegerField` -
`BooleanField` - `DateField` - `ChoiceField` - `FileField` -
`ImageField`

Each field performs validation based on its type.

------------------------------------------------------------------------

## Form Rendering

Rendering is the process of displaying a form in an HTML template.

Methods: - `{{ form }}` - `{{ form.as_p }}` - `{{ form.as_table }}` -
`{{ form.as_ul }}` - Manual rendering (`{{ form.name }}`,
`{{ form.email }}`)

Manual rendering offers the greatest control over layout and styling.

------------------------------------------------------------------------

## GET and POST Forms

### GET

-   Used to retrieve data.
-   Data is appended to the URL.
-   Suitable for searches and filters.
-   Not recommended for sensitive information.

### POST

-   Used to submit data.
-   Data is sent in the request body.
-   Suitable for creating or updating data.
-   Used with forms that modify server data.

------------------------------------------------------------------------

## CSRF Protection

CSRF (Cross-Site Request Forgery) is an attack where a malicious site
tricks a logged-in user into submitting unwanted requests.

Django prevents this using a CSRF token.

Every POST form should include:

``` html
{% csrf_token %}
```

If the token is missing, Django rejects the request.

------------------------------------------------------------------------

## Form Validation

Validation checks whether submitted data is correct before processing or
saving it.

Validation occurs when:

``` python
form.is_valid()
```

If validation succeeds: - `True` - Cleaned data becomes available
through `form.cleaned_data`

If validation fails: - Errors are stored in `form.errors`

------------------------------------------------------------------------

## Built-in Validators

Django provides validators for common validation rules.

Examples: - `MinLengthValidator` - `MaxLengthValidator` -
`MinValueValidator` - `MaxValueValidator` - `RegexValidator`

They help enforce constraints without writing custom logic.

------------------------------------------------------------------------

## Custom Validation

Custom validation is used when built-in validators are not sufficient.

Types: - Field-level validation using `clean_<fieldname>()` - Form-level
validation using `clean()`

This is useful for business rules or validating multiple fields
together.

------------------------------------------------------------------------

## Error Messages

When validation fails, Django automatically generates error messages.

Errors can be displayed: - For the entire form (`{{ form.errors }}`) -
For individual fields (`{{ form.field.errors }}`)

Developers can also define custom error messages for a better user
experience.

------------------------------------------------------------------------

## ModelForm

A ModelForm is a form automatically generated from a Django model.

Advantages: - No need to define fields manually. - Uses model
validation. - Can save directly to the database. - Reduces boilerplate
code.

Ideal for CRUD applications.

------------------------------------------------------------------------

## Saving Form Data

### Using `forms.Form`

Developers manually create and save the model instance using
`cleaned_data`.

### Using `ModelForm`

After validation, data can be saved directly:

``` python
form.save()
```

Internally, Django: 1. Creates a model instance. 2. Assigns validated
values. 3. Calls the model's `save()` method. 4. Stores the record in
the database.

------------------------------------------------------------------------

## Summary

-   HTML forms require manual handling.
-   Django Forms automate rendering, validation, and error handling.
-   Form fields define expected input types.
-   GET retrieves data; POST submits data.
-   CSRF protects against forged requests.
-   Validation ensures correct input.
-   Built-in and custom validators enforce rules.
-   Error messages provide user feedback.
-   ModelForms connect forms with models.
-   `form.save()` stores validated data in the database.
