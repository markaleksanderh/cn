from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.urls import reverse

from django.forms import ModelForm

class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)
    first_name = models.CharField(max_length=100, blank=True)
    second_name = models.CharField(max_length=100, blank=True)
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.username

class Job(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a job name")
    description = models.TextField(max_length=750, help_text="Enter job description", null=True, blank=True)
    value = models.IntegerField(null=True, blank=True, help_text="Enter job value")
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True)
    added = models.DateTimeField(auto_now_add=True)
    region = models.ForeignKey('Region', on_delete=models.SET_NULL, null=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('job_detail', args=[str(self.id)])

class JobQuote(models.Model):
    value = models.IntegerField(null=True, blank=True)
    quote_added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    job = models.ForeignKey('Job', on_delete=models.SET_NULL, null=True)



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
