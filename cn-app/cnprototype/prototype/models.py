from django.contrib.auth.models import AbstractUser
from django.db import models

from django.forms import ModelForm


# Create your models here.

"""
LIST MODELS
-- Job
-- Company

???
-- Region
-- Job type
"""

class CustomUser(AbstractUser):
    # First/last name is not a global-friendly pattern
    name = models.CharField(blank=True, max_length=255)
    first_name = models.CharField(max_length=100, blank=True)
    second_name = models.CharField(max_length=100, blank=True)
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.first_name

class Job(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a job name")
    description = models.CharField(max_length=1000, help_text="Enter job description", null=True, blank=True)
    value = models.IntegerField(null=True, blank=True, help_text="Enter job value")
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True)
    added = models.DateTimeField(auto_now_add=True)
    region = models.ForeignKey('Region', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=100, help_text="Enter company name")
    postcode = models.CharField(max_length=10, help_text="Enter company postcode", null=True)
    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=100, help_text="Enter region")
    def __str__(self):
        return self.name

class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = ['name', 'region']
