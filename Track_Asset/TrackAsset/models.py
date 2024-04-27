from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []


class Subscriber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)



class Company(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete = models.SET_NULL, null=True)

class Company_Assets(models.Model):
    company = models.ForeignKey(Company, on_delete = models.SET_NULL, null=True)
    employee = models.ForeignKey(Employee, on_delete = models.SET_NULL, null=True)
    device = models.CharField(max_length=100,null=True, blank=True)
    condition_choices = [
        ('Good', 'Good'),
        ('Fair', 'Fair'),
        ('Poor', 'Poor'),
    ]
    checked_out = models.DateTimeField()
    returned_in = models.DateTimeField(null=True, blank=True)
    condition_when_checked_out = models.CharField(max_length=10, choices=condition_choices,null=True, blank=True)
    condition_when_returned = models.CharField(max_length=10, choices=condition_choices, null=True, blank=True)



