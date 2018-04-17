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

    def __str__(self):
        return self.email


#
#
class Job(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a job name")
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True)
    added = models.DateField(null=True, blank=True)
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
