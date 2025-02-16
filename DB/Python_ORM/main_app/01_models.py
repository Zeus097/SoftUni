from django.db import models
from datetime import date

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=30)
    email_address = models.EmailField()
    photo = models.URLField()
    birth_date = models.DateField()
    works_full_time = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True)


CITIES = (

    ("Sofia", "Sofia"),
    ("Plovdiv", "Plovdiv"),
    ("Burgas", "Burgas"),
    ("Varna", "Varna")

)


class Department(models.Model):

    code = models.CharField(max_length=4, unique=True, primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    employees_count = models.PositiveIntegerField(default=1, verbose_name='Employees Count')
    location = models.CharField(max_length=20, choices=CITIES, null=True, blank=True)
    last_edited_on = models.DateTimeField(auto_now=True, editable=False)


class Project(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    budget = models.DecimalField(null=True, max_digits=10, decimal_places=2)
    duration_in_days = models.PositiveIntegerField(null=True, blank=True, verbose_name='Duration in Days')
    estimated_hours = models.FloatField(null=True, blank=True, verbose_name='Estimated Hours')
    start_date = models.DateField(verbose_name='Start Date', null=True, blank=True, default=date.today)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    last_edited_on = models.DateTimeField(auto_now=True, editable=False)
