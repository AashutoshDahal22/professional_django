## Models,Database and Django ORM

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

