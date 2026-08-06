# QuerySets in Django ORM

## What is a QuerySet?

A **QuerySet** is a collection of objects retrieved from the database.

Whenever you query the database using Django's ORM, Django returns the results as a **QuerySet**.

Think of a QuerySet as the Django equivalent of the results returned by an SQL query.

---

## SQL vs Django ORM

### SQL

```sql
SELECT * FROM students;
```

### Django ORM

```python
Student.objects.all()
```

Both statements retrieve **all student records** from the database.

The difference is that Django uses Python code instead of writing raw SQL.

---

# Common QuerySet Examples

## Retrieve All Records

```python
Student.objects.all()
```

Returns every student stored in the database.

---

## Filter Records

Retrieve students belonging to the **IT** department.

```python
Student.objects.filter(
    department__name="IT"
)
```

The `__` (double underscore) is Django's lookup syntax used to access fields in related models.

---

Retrieve students older than 20.

```python
Student.objects.filter(
    age__gt=20
)
```

Here,

- `gt` = Greater Than (`>`)

---

## Retrieve the First Record

```python
Student.objects.first()
```

Returns the first student in the QuerySet.

---

## Count Records

```python
Student.objects.count()
```

Returns the total number of student records.

---

## Order Records

Sort students alphabetically by first name.

```python
Student.objects.order_by("first_name")
```

---

Sort students by age in descending order.

```python
Student.objects.order_by("-age")
```

The minus sign (`-`) indicates descending order.

Without the minus sign, Django sorts in ascending order.

---

# QuerySets are Lazy

One of Django ORM's biggest advantages is that **QuerySets are lazy**.

This means Django **does not immediately execute the SQL query** when you create a QuerySet.

For example,

```python
students = Student.objects.all()
```

At this point, **no database query has been executed yet**.

The query is only executed when Django actually needs the data.

For example,

```python
for student in students:
    print(student.name)
```

or

```python
print(students)
```

or

```python
list(students)
```

Only then does Django send the SQL query to the database.

---

# Why is this Useful?

Lazy evaluation allows Django to optimize database access.

Instead of executing multiple unnecessary queries, Django waits until the data is actually required.

This improves:

- Application performance
- Database efficiency
- Memory usage

---

# Summary

| QuerySet Method | Description                           |
| --------------- | ------------------------------------- |
| `all()`         | Retrieve all records                  |
| `filter()`      | Retrieve records matching a condition |
| `first()`       | Retrieve the first record             |
| `count()`       | Count the number of records           |
| `order_by()`    | Sort records                          |
| `exclude()`     | Exclude matching records              |
| `get()`         | Retrieve a single object              |
| `exists()`      | Check whether records exist           |

---

# Django ORM Relationships & Optimization Notes

# Related Objects

## Definition

A **Related Object** is an object that is connected to another object through a relationship such as a **ForeignKey**, **OneToOneField**, or **ManyToManyField**.

Instead of storing all the information inside one table, databases store related information in separate tables and connect them using relationships.

---

## Example

Imagine a college database.

### Course Table

| Course ID | Course Name |
|------------|-------------|
| 1 | Python |
| 2 | Django |
| 3 | React |

### Student Table

| Student | Course ID |
|----------|-----------|
| John | 2 |
| Jane | 1 |
| Alex | 2 |

Notice that the Student table does **not** store the course name.

Instead, it stores the **Course ID**, which points to a record inside the Course table.

When Django needs the course information, it automatically follows this relationship and retrieves the related Course object.

---

## Why use Related Objects?

Instead of duplicating information in multiple tables, related objects:

- Reduce data duplication
- Keep the database organized
- Maintain data consistency
- Make querying data much easier

---

# Reverse Relationships

## Definition

A reverse relationship allows us to start from the related model and retrieve all objects connected to it.

Normally we think:

```
Student
    ↓
Course
```

A reverse relationship allows us to think:

```
Course
    ↓
Students
```

For example,

Instead of asking:

> Which course does John study?

We ask:

> Which students study Django?

Reverse relationships allow Django to retrieve every student connected to a specific course.

---

# Database Queries

Whenever Django needs data from the database, it sends a **database query**.

For example:

- Retrieve all students
- Retrieve one course
- Retrieve all contacts

Every query takes time.

A few queries are not a problem.

Thousands of unnecessary queries can slow down an application.

Therefore, reducing database queries improves application performance.

---

# The N+1 Query Problem

One of the most common performance issues in Django is called the **N+1 Query Problem**.

Imagine we have:

- 100 students
- Each student belongs to one course

Django first retrieves all students.

After that, for every student, it retrieves the related course separately.

This means:

- 1 query to retrieve all students
- 100 additional queries to retrieve every student's course

Total:

```
1 + 100 = 101 Queries
```

As the number of records increases, the application becomes slower because it keeps asking the database for related information.

---

# select_related()

## Definition

`select_related()` is an ORM optimization method used to retrieve related objects **in a single database query**.

Instead of retrieving Students first and Courses later, Django retrieves both tables together.

Internally, Django performs an SQL JOIN.

---

## When to use select_related()

Use `select_related()` when working with:

- ForeignKey
- OneToOneField

These relationships return only one related object, making SQL JOINs efficient.

---

## Advantages

- Reduces the number of database queries
- Improves application performance
- Makes page loading faster
- Prevents the N+1 Query Problem

---

## Easy Way to Remember

> **Select the related object together with the main object.**

---

# Many-to-Many Relationships

Sometimes one object can be connected to many other objects.

Example:

A student can study:

- Python
- Django
- React

Likewise,

Each course can have many students.

This is called a **Many-to-Many Relationship**.

---

# prefetch_related()

## Definition

`prefetch_related()` is another ORM optimization method.

Unlike `select_related()`, Django does **not** retrieve everything using one SQL JOIN.

Instead, Django:

1. Retrieves the main objects.
2. Retrieves the related objects.
3. Combines the results in Python.

This approach is much more efficient for Many-to-Many relationships.

---

## When to use prefetch_related()

Use `prefetch_related()` when working with:

- ManyToManyField
- Reverse ForeignKey relationships
- Reverse One-to-Many relationships

---

## Advantages

- Prevents excessive database queries
- Optimizes complex relationships
- Improves application performance
- Reduces unnecessary database communication

---

# select_related() vs prefetch_related()

| select_related() | prefetch_related() |
|------------------|--------------------|
| Used for ForeignKey | Used for ManyToManyField |
| Used for OneToOneField | Used for Reverse Relationships |
| Uses SQL JOIN | Uses Separate Queries |
| Retrieves everything together | Retrieves separately and combines later |
| Usually performs a single query | Performs multiple optimized queries |

---

# ORM Optimization

## Definition

ORM Optimization is the process of reducing unnecessary database queries while retrieving the same data.

The goal is **not** to retrieve different data.

The goal is to retrieve the **same data more efficiently**.

---

## Why is ORM Optimization Important?

Database operations are one of the slowest parts of a web application.

Reducing unnecessary database queries leads to:

- Faster websites
- Better user experience
- Lower server load
- Better scalability
- Improved application performance

---

# Real-Life Analogy

Imagine going grocery shopping.

### Without Optimization

You need:

- Milk
- Bread
- Eggs

You make three separate trips.

```
Home
 ↓
Store
 ↓
Home
 ↓
Store
 ↓
Home
```

This takes unnecessary time.

---

### With Optimization

Instead, you make a shopping list.

Buy everything in one trip.

```
Home
      ↓
Store
      ↓
Home
```

You bought the same items.

You simply reduced the number of trips.

Database optimization works exactly the same way.

---

# Key Takeaways

- A **Related Object** is an object connected through a relationship.
- Relationships allow data to be stored efficiently without duplication.
- Reverse relationships allow us to retrieve related objects from the opposite direction.
- Every interaction with the database requires a query.
- Too many database queries reduce application performance.
- The **N+1 Query Problem** occurs when Django repeatedly queries related objects.
- `select_related()` solves this problem for **ForeignKey** and **OneToOneField** relationships.
- `prefetch_related()` solves this problem for **Many-to-Many** and reverse relationships.
- ORM Optimization is about retrieving the **same data with fewer database queries**, resulting in faster and more efficient applications.