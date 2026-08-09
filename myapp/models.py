from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Students(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="students"
    )
    is_active = models.BooleanField(default=True)
    joined_date = models.DateField(auto_now_add=True)

    # this make sure that in the admin panel we don't see object instead it returns the actual name of the user

    # if we are using the decorator in admin.py we can comment this out
    # def __str__(self):
    #     return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    
    image = models.ImageField(
        upload_to="contacts/",
        blank=True,
        null=True
    )

    # this make sure that in the admin panel we don't see object instead it returns the actual name of the user

    # if we are using the decorator in admin.py we can comment this out
    # def __str__(self):
    #     return self.name
