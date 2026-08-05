from django.db import models

class Students(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    course = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name